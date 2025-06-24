@description('Location for the resource')
param location string

@minLength(4)
@maxLength(63)
@description('Name of the Log Analytics workspace')
param logAnalyticsName string

@description('Tags to apply to resources')
param tags object

@description('User Assigned Identity Principal ID for access control')
param userAssignedIdentityPrincipalId string

resource logAnalytics 'Microsoft.OperationalInsights/workspaces@2022-10-01' =  {
  name: logAnalyticsName
  location: location
  tags: tags
  properties: {
    sku: {
      name: 'PerGB2018'
    }
    retentionInDays: 30
  }
}

resource appInsights 'Microsoft.Insights/components@2020-02-02' = {
  name: 'appinsights-${logAnalyticsName}'
  location: location
  kind: 'web'
  tags: tags
  properties: {
    Application_Type: 'web'
    WorkspaceResourceId: logAnalytics.id
    IngestionMode: 'LogAnalytics'
    publicNetworkAccessForIngestion: 'Enabled'
    publicNetworkAccessForQuery: 'Enabled'
  }
}



// Assign the User Assigned Identity Contributor role
resource storageAccountRoleAssignment 'Microsoft.Authorization/roleAssignments@2020-04-01-preview' = {
  name: guid(appInsights.id, userAssignedIdentityPrincipalId, 'Monitoring Contributor')
  scope: appInsights
  properties: {
    roleDefinitionId: resourceId('Microsoft.Authorization/roleDefinitions', '749f88d5-cbae-40b8-bcfc-e573ddc772fa') // Role definition ID for Cognitive Services OpenAI User
    principalId: userAssignedIdentityPrincipalId
    principalType: 'ServicePrincipal'
  }
}



output logAnalyticsId string = logAnalytics.id 
output appInsightsName string = appInsights.name 
output appInsightsInstrumentationKey string = appInsights.properties.InstrumentationKey
output appInsightsConnectionString string = appInsights.properties.ConnectionString 
output logAnalyticsWorkspaceId string = logAnalytics.id
output logAnalyticsWorkspaceName string = logAnalytics.name
