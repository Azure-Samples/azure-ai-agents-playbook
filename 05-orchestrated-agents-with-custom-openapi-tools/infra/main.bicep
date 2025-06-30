targetScope = 'subscription'

@minLength(1)
@maxLength(64)
@description('Name of the environment that can be used as part of naming resource convention')
param environmentName string

@minLength(1)
@description('Primary location for all resources')
param location string = 'swedencentral'

@minLength(1)
@maxLength(32)
@description('Name of the resource group')
param rgName string


@description('GitHub repository URL containing the document processor code.')
param gitHubRepoUrl string = 'https://github.com/Azure-Samples/azure-ai-agents-playbook'

@description('GitHub repository branch to use.')
param gitHubRepoBranch string = 'main'

@description('Dockerfile path relative to the repository root.')
param dockerfilePath string = '05-orchestrated-agents-with-custom-openapi-tools/Dockerfile'

resource resourceGroup 'Microsoft.Resources/resourceGroups@2021-04-01' = {
  name: '${abbrs.resourcesResourceGroup}-${rgName}'
  location: location
  tags: tags
}

var resourceGroupName = resourceGroup.name
var randomSuffix = uniqueString(subscription().id, resourceGroupName, environmentName)


var uniqueId = uniqueString(resourceGroup.id)

var tags = {
  'azd-env-name': environmentName
}

var abbrs = {
  resourcesResourceGroup: 'rg'
  containerAppsEnvironment: 'cae'
  containerRegistry: 'cr'
  logAnalyticsWorkspace: 'law'
  containerApp: 'ca'
}


module uami 'modules/uami.bicep' = {
  name: 'uami'
  scope: resourceGroup
  params: {
    uniqueId: uniqueId
    prefix: 'afa-${randomSuffix}-'
    location: location
  }
}

module monitoring 'modules/monitoring.bicep' = {
  name: 'monitoring'
  scope: resourceGroup
  params: {
    location: location
    tags: tags
    logAnalyticsName: '${abbrs.logAnalyticsWorkspace}-${take(environmentName, 10)}-${randomSuffix}'
    userAssignedIdentityPrincipalId: uami.outputs.principalId
  }
}

module registry 'modules/container-registry.bicep' = {
  name: 'registry'
  scope: resourceGroup
  params: {
    location: location
    tags: tags
    containerRegistryName: '${abbrs.containerRegistry}${environmentName}${randomSuffix}'
    userAssignedIdentityPrincipalId: uami.outputs.principalId
  }
}

module containerApps 'modules/container-apps.bicep' = {
  name: 'container-apps'
  scope: resourceGroup
  params: {
    location: location
    tags: tags
    containerAppsEnvironmentName: '${abbrs.containerAppsEnvironment}-${environmentName}-${randomSuffix}'
    logAnalyticsWorkspaceName: monitoring.outputs.logAnalyticsWorkspaceName
  }
}

// Build and push the container image to ACR
module acrBuild 'modules/acr-build.bicep' = {
  name: 'acr-build-deployment'
  scope: resourceGroup
  params: {
    acrName: registry.outputs.name
    location: location
    gitHubRepoUrl: gitHubRepoUrl
    gitHubBranch: gitHubRepoBranch
    dockerfilePath: dockerfilePath
    imageName: 'agents-fast-plugins:latest'
    timestamp: 'timestamp-${deployment().name}'
  }
  dependsOn: [
    monitoring
    containerApps
  ]
}

module app 'modules/app.bicep' = {
  name: 'app'
  scope: resourceGroup
  params: {
    location: location
    tags: tags
    containerAppsEnvironmentId: containerApps.outputs.id
    containerRegistryServer: registry.outputs.loginServer
    imageName: 'agents-fast-plugins:latest'
    targetPort: 80
    containerAppName: '${abbrs.containerApp}-${environmentName}-${randomSuffix}'
    userAssignedIdentityPrincipalId: uami.outputs.identityId
  }
  dependsOn: [
    acrBuild
  ]
}

output AZURE_LOCATION string = location
output AZURE_CONTAINER_REGISTRY_ENDPOINT string = registry.outputs.loginServer
output AZURE_CONTAINER_APP_NAME string = app.outputs.name
output AZURE_CONTAINER_APP_ENDPOINT string = app.outputs.uri
