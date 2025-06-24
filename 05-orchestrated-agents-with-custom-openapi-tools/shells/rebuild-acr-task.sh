#!/bin/bash

# Script to rebuild container image using ACR Tasks
# This approach builds directly from GitHub without requiring local Docker

# Configuration - default values from main.bicep
RESOURCE_GROUP=""
ACR_NAME=""
GIT_REPO="https://github.com/Azure-Samples/azure-ai-agents-playbook"
GIT_BRANCH="main"
IMAGE_NAME="agents-fast-plugins"
IMAGE_TAG="latest"
DOCKERFILE_PATH="05-orchestrated-agents-with-custom-openapi-tools/Dockerfile"  # Path relative to repo root

# Parse command line arguments
while [[ $# -gt 0 ]]; do
  case $1 in
    --resource-group|-g)
      RESOURCE_GROUP="$2"
      shift 2
      ;;
    --acr-name|-a)
      ACR_NAME="$2"
      shift 2
      ;;
    --git-repo|-r)
      GIT_REPO="$2"
      shift 2
      ;;
    --git-branch|-b)
      GIT_BRANCH="$2"
      shift 2
      ;;
    --image-name|-i)
      IMAGE_NAME="$2"
      shift 2
      ;;
    --image-tag|-t)
      IMAGE_TAG="$2"
      shift 2
      ;;
    --dockerfile-path|-d)
      DOCKERFILE_PATH="$2"
      shift 2
      ;;
    --help|-h)
      echo "Usage: $0 [options]"
      echo "Options:"
      echo "  --resource-group, -g     Resource group name containing the ACR"
      echo "  --acr-name, -a           Name of the Azure Container Registry"
      echo "  --git-repo, -r           Git repository URL (default: $GIT_REPO)"
      echo "  --git-branch, -b         Git branch name (default: $GIT_BRANCH)"
      echo "  --image-name, -i         Name of the container image (default: $IMAGE_NAME)"
      echo "  --image-tag, -t          Tag for the container image (default: $IMAGE_TAG)"
      echo "  --dockerfile-path, -d    Path to the Dockerfile relative to repo root (default: $DOCKERFILE_PATH)"
      echo "  --help, -h               Show this help message"
      exit 0
      ;;
    *)
      echo "Unknown parameter: $1"
      exit 1
      ;;
  esac
done

# Check required parameters
if [[ -z "$RESOURCE_GROUP" ]]; then
  echo "Error: Resource group name is required (--resource-group)"
  exit 1
fi

if [[ -z "$ACR_NAME" ]]; then
  echo "Error: ACR name is required (--acr-name)"
  exit 1
fi

# Ensure user is logged in to Azure
echo "Checking Azure login status..."
ACCOUNT=$(az account show --query name -o tsv 2>/dev/null)
if [[ -z "$ACCOUNT" ]]; then
  echo "You are not logged in to Azure. Please run 'az login' first."
  exit 1
fi
echo "Logged in as: $ACCOUNT"

# Get ACR login server
echo "Getting ACR login server..."
ACR_LOGIN_SERVER=$(az acr show --name "$ACR_NAME" --resource-group "$RESOURCE_GROUP" --query loginServer -o tsv)
if [[ -z "$ACR_LOGIN_SERVER" ]]; then
  echo "Error: Could not retrieve ACR login server. Please check the ACR name and resource group."
  exit 1
fi
echo "ACR Login Server: $ACR_LOGIN_SERVER"

# Create a timestamp to make the run unique
TIMESTAMP=$(date +%Y%m%d%H%M%S)
RUN_ID="rebuild-${TIMESTAMP}"

# Run ACR task to build the image directly from GitHub
echo "Starting ACR Task to build the image..."
echo "Building from GitHub repository: ${GIT_REPO}#${GIT_BRANCH}"

az acr build \
  --registry "$ACR_NAME" \
  --resource-group "$RESOURCE_GROUP" \
  --image "${IMAGE_NAME}:${IMAGE_TAG}" \
  --file "${DOCKERFILE_PATH}" \
  --build-arg BRANCH="$GIT_BRANCH" \
  "${GIT_REPO}#${GIT_BRANCH}"

BUILD_SUCCESS=$?

if [ $BUILD_SUCCESS -eq 0 ]; then
  echo "Image build task complete: ${ACR_LOGIN_SERVER}/${IMAGE_NAME}:${IMAGE_TAG}"
  echo "Your Container App will pull this new image the next time it runs."
else
  echo "Error: Image build failed with exit code $BUILD_SUCCESS"
  exit $BUILD_SUCCESS
fi