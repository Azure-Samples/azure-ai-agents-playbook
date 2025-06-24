@description('Name of the Azure Container Registry')
param acrName string

@description('Location for resources')
param location string

@description('GitHub repository URL containing the document processor code')
param gitHubRepoUrl string

@description('GitHub repository branch to use')
param gitHubBranch string = 'main'

@description('Dockerfile path relative to the repository root')
param dockerfilePath string

@description('Name and tag for the container image')
param imageName string

@description('Timestamp to force task run updates')
param timestamp string = utcNow()

resource containerRegistry 'Microsoft.ContainerRegistry/registries@2023-01-01-preview' existing = {
  name: acrName
}

resource acrBuildTask 'Microsoft.ContainerRegistry/registries/taskRuns@2019-06-01-preview' = {
  name: guid('${acrName}-build-task-${imageName}')
  parent: containerRegistry
  location: location
  properties: {
    forceUpdateTag: timestamp
    runRequest: {
      type: 'DockerBuildRequest'
      sourceLocation: gitHubRepoUrl
      platform: {
        os: 'Linux'
        architecture: 'amd64'
      }
      dockerFilePath: dockerfilePath
      imageNames: [
        imageName
      ]
      isPushEnabled: true
      isArchiveEnabled: false
      timeout: 28800
      agentConfiguration: {
        cpu: 2
      }
      arguments: [
        {
          name: 'branch'
          value: gitHubBranch
        }
      ]
    }
  }
}

output buildTaskId string = acrBuildTask.id
output buildTaskName string = acrBuildTask.name
