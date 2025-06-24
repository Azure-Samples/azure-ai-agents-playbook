param containerAppName string
param location string
param tags object = {}
param containerAppsEnvironmentId string
param containerRegistryServer string
param imageName string
param targetPort int
param env array = []

@description('User Assigned Identity Principal ID for access control')
param userAssignedIdentityPrincipalId string



resource containerApp 'Microsoft.App/containerApps@2023-05-01' = {
  name: containerAppName
  location: location
  tags: tags
  identity: {
    type: 'UserAssigned'
    userAssignedIdentities: {
      '${userAssignedIdentityPrincipalId}': {}
    }
  }
  properties: {
    managedEnvironmentId: containerAppsEnvironmentId
    configuration: {
      ingress: {
        external: true
        targetPort: targetPort
        allowInsecure: false
        traffic: [
          {
            latestRevision: true
            weight: 100
          }
        ]
      }
      registries: [
        {
          server: containerRegistryServer
          identity: userAssignedIdentityPrincipalId
        }
      ]
    }
    template: {
      containers: [
        {
          name: 'main'
          image: '${containerRegistryServer}/${imageName}'
          resources: {
            cpu: json('0.5')
            memory: '1Gi'
          }
          env: env
        }
      ]
      scale: {
        minReplicas: 1
        maxReplicas: 10
      }
    }
  }
}

output name string = containerApp.name
output uri string = 'https://${containerApp.properties.configuration.ingress.fqdn}'
