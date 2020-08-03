# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse

from .. import models


class BookmarksOperations(object):
    """BookmarksOperations operations.

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
            self, resource_group_name, operational_insights_resource_provider, workspace_name, custom_headers=None, raw=False, **operation_config):
        """Gets all bookmarks.

        :param resource_group_name: The name of the resource group within the
         user's subscription. The name is case insensitive.
        :type resource_group_name: str
        :param operational_insights_resource_provider: The namespace of
         workspaces resource provider- Microsoft.OperationalInsights.
        :type operational_insights_resource_provider: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: BookmarkList or ClientRawResponse if raw=true
        :rtype: ~securityinsights.models.BookmarkList or
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
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', max_length=90, min_length=1)
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
            deserialized = self._deserialize('BookmarkList', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{operationalInsightsResourceProvider}/workspaces/{workspaceName}/providers/Microsoft.SecurityInsights/bookmarks'}

    def get(
            self, resource_group_name, operational_insights_resource_provider, workspace_name, bookmark_id, custom_headers=None, raw=False, **operation_config):
        """Gets a bookmark.

        :param resource_group_name: The name of the resource group within the
         user's subscription. The name is case insensitive.
        :type resource_group_name: str
        :param operational_insights_resource_provider: The namespace of
         workspaces resource provider- Microsoft.OperationalInsights.
        :type operational_insights_resource_provider: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param bookmark_id: Bookmark ID
        :type bookmark_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Bookmark or ClientRawResponse if raw=true
        :rtype: ~securityinsights.models.Bookmark or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`CloudErrorException<securityinsights.models.CloudErrorException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str', pattern=r'^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'operationalInsightsResourceProvider': self._serialize.url("operational_insights_resource_provider", operational_insights_resource_provider, 'str'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', max_length=90, min_length=1),
            'bookmarkId': self._serialize.url("bookmark_id", bookmark_id, 'str')
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
            deserialized = self._deserialize('Bookmark', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{operationalInsightsResourceProvider}/workspaces/{workspaceName}/providers/Microsoft.SecurityInsights/bookmarks/{bookmarkId}'}

    def create_or_update(
            self, resource_group_name, operational_insights_resource_provider, workspace_name, bookmark_id, bookmark, custom_headers=None, raw=False, **operation_config):
        """Creates or updates the bookmark.

        :param resource_group_name: The name of the resource group within the
         user's subscription. The name is case insensitive.
        :type resource_group_name: str
        :param operational_insights_resource_provider: The namespace of
         workspaces resource provider- Microsoft.OperationalInsights.
        :type operational_insights_resource_provider: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param bookmark_id: Bookmark ID
        :type bookmark_id: str
        :param bookmark: The bookmark
        :type bookmark: ~securityinsights.models.Bookmark
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Bookmark or ClientRawResponse if raw=true
        :rtype: ~securityinsights.models.Bookmark or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`CloudErrorException<securityinsights.models.CloudErrorException>`
        """
        # Construct URL
        url = self.create_or_update.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str', pattern=r'^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'operationalInsightsResourceProvider': self._serialize.url("operational_insights_resource_provider", operational_insights_resource_provider, 'str'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', max_length=90, min_length=1),
            'bookmarkId': self._serialize.url("bookmark_id", bookmark_id, 'str')
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
        body_content = self._serialize.body(bookmark, 'Bookmark')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 201]:
            raise models.CloudErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Bookmark', response)
        if response.status_code == 201:
            deserialized = self._deserialize('Bookmark', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{operationalInsightsResourceProvider}/workspaces/{workspaceName}/providers/Microsoft.SecurityInsights/bookmarks/{bookmarkId}'}

    def delete(
            self, resource_group_name, operational_insights_resource_provider, workspace_name, bookmark_id, custom_headers=None, raw=False, **operation_config):
        """Delete the bookmark.

        :param resource_group_name: The name of the resource group within the
         user's subscription. The name is case insensitive.
        :type resource_group_name: str
        :param operational_insights_resource_provider: The namespace of
         workspaces resource provider- Microsoft.OperationalInsights.
        :type operational_insights_resource_provider: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param bookmark_id: Bookmark ID
        :type bookmark_id: str
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
        url = self.delete.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str', pattern=r'^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'operationalInsightsResourceProvider': self._serialize.url("operational_insights_resource_provider", operational_insights_resource_provider, 'str'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', max_length=90, min_length=1),
            'bookmarkId': self._serialize.url("bookmark_id", bookmark_id, 'str')
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
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{operationalInsightsResourceProvider}/workspaces/{workspaceName}/providers/Microsoft.SecurityInsights/bookmarks/{bookmarkId}'}