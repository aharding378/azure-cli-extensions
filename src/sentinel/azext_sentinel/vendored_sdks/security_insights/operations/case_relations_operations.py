# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse

from .. import models


class CaseRelationsOperations(object):
    """CaseRelationsOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: API version for the operation. Constant value: "2019-01-01-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config
        self.api_version = "2019-01-01-preview"

    def list(
            self, resource_group_name, operational_insights_resource_provider, workspace_name, case_id, filter=None, orderby=None, top=None, skip_token=None, custom_headers=None, raw=False, **operation_config):
        """Gets all case relations.

        :param resource_group_name: The name of the resource group within the
         user's subscription. The name is case insensitive.
        :type resource_group_name: str
        :param operational_insights_resource_provider: The namespace of
         workspaces resource provider- Microsoft.OperationalInsights.
        :type operational_insights_resource_provider: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param case_id: Case ID
        :type case_id: str
        :param filter: Filters the results, based on a Boolean condition.
         Optional.
        :type filter: str
        :param orderby: Sorts the results. Optional.
        :type orderby: str
        :param top: Returns only the first n results. Optional.
        :type top: int
        :param skip_token: Skiptoken is only used if a previous operation
         returned a partial result. If a previous response contains a nextLink
         element, the value of the nextLink element will include a skiptoken
         parameter that specifies a starting point to use for subsequent calls.
         Optional.
        :type skip_token: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: CaseRelationList or ClientRawResponse if raw=true
        :rtype: ~securityinsights.models.CaseRelationList or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`CloudErrorException<securityinsights.models.CloudErrorException>`
        """
        # Construct URL
        url = self.list.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str', pattern=r'^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'operationalInsightsResourceProvider': self._serialize.url("operational_insights_resource_provider", operational_insights_resource_provider, 'str'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', max_length=90, min_length=1),
            'caseId': self._serialize.url("case_id", case_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        if filter is not None:
            query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
        if orderby is not None:
            query_parameters['$orderby'] = self._serialize.query("orderby", orderby, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query("top", top, 'int')
        if skip_token is not None:
            query_parameters['$skipToken'] = self._serialize.query("skip_token", skip_token, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.CloudErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('CaseRelationList', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{operationalInsightsResourceProvider}/workspaces/{workspaceName}/providers/Microsoft.SecurityInsights/cases/{caseId}/relations'}

    def get_relation(
            self, resource_group_name, operational_insights_resource_provider, workspace_name, case_id, relation_name, custom_headers=None, raw=False, **operation_config):
        """Gets a case relation.

        :param resource_group_name: The name of the resource group within the
         user's subscription. The name is case insensitive.
        :type resource_group_name: str
        :param operational_insights_resource_provider: The namespace of
         workspaces resource provider- Microsoft.OperationalInsights.
        :type operational_insights_resource_provider: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param case_id: Case ID
        :type case_id: str
        :param relation_name: Relation Name
        :type relation_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: CaseRelation or ClientRawResponse if raw=true
        :rtype: ~securityinsights.models.CaseRelation or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`CloudErrorException<securityinsights.models.CloudErrorException>`
        """
        # Construct URL
        url = self.get_relation.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str', pattern=r'^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'operationalInsightsResourceProvider': self._serialize.url("operational_insights_resource_provider", operational_insights_resource_provider, 'str'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', max_length=90, min_length=1),
            'caseId': self._serialize.url("case_id", case_id, 'str'),
            'relationName': self._serialize.url("relation_name", relation_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.CloudErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('CaseRelation', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_relation.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{operationalInsightsResourceProvider}/workspaces/{workspaceName}/providers/Microsoft.SecurityInsights/cases/{caseId}/relations/{relationName}'}

    def create_or_update_relation(
            self, resource_group_name, operational_insights_resource_provider, workspace_name, case_id, relation_name, relation_input_model, custom_headers=None, raw=False, **operation_config):
        """Creates or updates the case relation.

        :param resource_group_name: The name of the resource group within the
         user's subscription. The name is case insensitive.
        :type resource_group_name: str
        :param operational_insights_resource_provider: The namespace of
         workspaces resource provider- Microsoft.OperationalInsights.
        :type operational_insights_resource_provider: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param case_id: Case ID
        :type case_id: str
        :param relation_name: Relation Name
        :type relation_name: str
        :param relation_input_model: The relation input model
        :type relation_input_model:
         ~securityinsights.models.RelationsModelInput
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: CaseRelation or ClientRawResponse if raw=true
        :rtype: ~securityinsights.models.CaseRelation or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`CloudErrorException<securityinsights.models.CloudErrorException>`
        """
        # Construct URL
        url = self.create_or_update_relation.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str', pattern=r'^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'operationalInsightsResourceProvider': self._serialize.url("operational_insights_resource_provider", operational_insights_resource_provider, 'str'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', max_length=90, min_length=1),
            'caseId': self._serialize.url("case_id", case_id, 'str'),
            'relationName': self._serialize.url("relation_name", relation_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(relation_input_model, 'RelationsModelInput')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 201]:
            raise models.CloudErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('CaseRelation', response)
        if response.status_code == 201:
            deserialized = self._deserialize('CaseRelation', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_or_update_relation.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{operationalInsightsResourceProvider}/workspaces/{workspaceName}/providers/Microsoft.SecurityInsights/cases/{caseId}/relations/{relationName}'}

    def delete_relation(
            self, resource_group_name, operational_insights_resource_provider, workspace_name, case_id, relation_name, custom_headers=None, raw=False, **operation_config):
        """Delete the case relation.

        :param resource_group_name: The name of the resource group within the
         user's subscription. The name is case insensitive.
        :type resource_group_name: str
        :param operational_insights_resource_provider: The namespace of
         workspaces resource provider- Microsoft.OperationalInsights.
        :type operational_insights_resource_provider: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param case_id: Case ID
        :type case_id: str
        :param relation_name: Relation Name
        :type relation_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`CloudErrorException<securityinsights.models.CloudErrorException>`
        """
        # Construct URL
        url = self.delete_relation.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str', pattern=r'^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'operationalInsightsResourceProvider': self._serialize.url("operational_insights_resource_provider", operational_insights_resource_provider, 'str'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', max_length=90, min_length=1),
            'caseId': self._serialize.url("case_id", case_id, 'str'),
            'relationName': self._serialize.url("relation_name", relation_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 204]:
            raise models.CloudErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    delete_relation.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{operationalInsightsResourceProvider}/workspaces/{workspaceName}/providers/Microsoft.SecurityInsights/cases/{caseId}/relations/{relationName}'}
