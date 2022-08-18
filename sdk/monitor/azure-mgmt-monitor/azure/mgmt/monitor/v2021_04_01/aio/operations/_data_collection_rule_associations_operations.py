# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._data_collection_rule_associations_operations import build_create_request, build_delete_request, build_get_request, build_list_by_resource_request, build_list_by_rule_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class DataCollectionRuleAssociationsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~$(python-base-namespace).v2021_04_01.aio.MonitorManagementClient`'s
        :attr:`data_collection_rule_associations` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")


    @distributed_trace
    def list_by_resource(
        self,
        resource_uri: str,
        **kwargs: Any
    ) -> AsyncIterable[_models.DataCollectionRuleAssociationProxyOnlyResourceListResult]:
        """Lists associations for the specified resource.

        Lists associations for the specified resource.

        :param resource_uri: The identifier of the resource.
        :type resource_uri: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either
         DataCollectionRuleAssociationProxyOnlyResourceListResult or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~$(python-base-namespace).v2021_04_01.models.DataCollectionRuleAssociationProxyOnlyResourceListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-04-01"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.DataCollectionRuleAssociationProxyOnlyResourceListResult]

        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_by_resource_request(
                    resource_uri=resource_uri,
                    api_version=api_version,
                    template_url=self.list_by_resource.metadata['url'],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                
                request = build_list_by_resource_request(
                    resource_uri=resource_uri,
                    api_version=api_version,
                    template_url=next_link,
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("DataCollectionRuleAssociationProxyOnlyResourceListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponseCommonV2, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_resource.metadata = {'url': "/{resourceUri}/providers/Microsoft.Insights/dataCollectionRuleAssociations"}  # type: ignore

    @distributed_trace
    def list_by_rule(
        self,
        resource_group_name: str,
        data_collection_rule_name: str,
        **kwargs: Any
    ) -> AsyncIterable[_models.DataCollectionRuleAssociationProxyOnlyResourceListResult]:
        """Lists associations for the specified data collection rule.

        Lists associations for the specified data collection rule.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param data_collection_rule_name: The name of the data collection rule. The name is case
         insensitive.
        :type data_collection_rule_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either
         DataCollectionRuleAssociationProxyOnlyResourceListResult or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~$(python-base-namespace).v2021_04_01.models.DataCollectionRuleAssociationProxyOnlyResourceListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-04-01"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.DataCollectionRuleAssociationProxyOnlyResourceListResult]

        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_by_rule_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    data_collection_rule_name=data_collection_rule_name,
                    api_version=api_version,
                    template_url=self.list_by_rule.metadata['url'],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                
                request = build_list_by_rule_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    data_collection_rule_name=data_collection_rule_name,
                    api_version=api_version,
                    template_url=next_link,
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("DataCollectionRuleAssociationProxyOnlyResourceListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponseCommonV2, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_rule.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/dataCollectionRules/{dataCollectionRuleName}/associations"}  # type: ignore

    @distributed_trace_async
    async def get(
        self,
        resource_uri: str,
        association_name: str,
        **kwargs: Any
    ) -> _models.DataCollectionRuleAssociationProxyOnlyResource:
        """Returns the specified association.

        Returns the specified association.

        :param resource_uri: The identifier of the resource.
        :type resource_uri: str
        :param association_name: The name of the association. The name is case insensitive.
        :type association_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DataCollectionRuleAssociationProxyOnlyResource, or the result of cls(response)
        :rtype:
         ~$(python-base-namespace).v2021_04_01.models.DataCollectionRuleAssociationProxyOnlyResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-04-01"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.DataCollectionRuleAssociationProxyOnlyResource]

        
        request = build_get_request(
            resource_uri=resource_uri,
            association_name=association_name,
            api_version=api_version,
            template_url=self.get.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponseCommonV2, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('DataCollectionRuleAssociationProxyOnlyResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/{resourceUri}/providers/Microsoft.Insights/dataCollectionRuleAssociations/{associationName}"}  # type: ignore


    @distributed_trace_async
    async def create(
        self,
        resource_uri: str,
        association_name: str,
        body: Optional[_models.DataCollectionRuleAssociationProxyOnlyResource] = None,
        **kwargs: Any
    ) -> _models.DataCollectionRuleAssociationProxyOnlyResource:
        """Creates or updates an association.

        Creates or updates an association.

        :param resource_uri: The identifier of the resource.
        :type resource_uri: str
        :param association_name: The name of the association. The name is case insensitive.
        :type association_name: str
        :param body: The payload. Default value is None.
        :type body:
         ~$(python-base-namespace).v2021_04_01.models.DataCollectionRuleAssociationProxyOnlyResource
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DataCollectionRuleAssociationProxyOnlyResource, or the result of cls(response)
        :rtype:
         ~$(python-base-namespace).v2021_04_01.models.DataCollectionRuleAssociationProxyOnlyResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-04-01"))  # type: str
        content_type = kwargs.pop('content_type', _headers.pop('Content-Type', "application/json"))  # type: Optional[str]
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.DataCollectionRuleAssociationProxyOnlyResource]

        if body is not None:
            _json = self._serialize.body(body, 'DataCollectionRuleAssociationProxyOnlyResource')
        else:
            _json = None

        request = build_create_request(
            resource_uri=resource_uri,
            association_name=association_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.create.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponseCommonV2, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('DataCollectionRuleAssociationProxyOnlyResource', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('DataCollectionRuleAssociationProxyOnlyResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create.metadata = {'url': "/{resourceUri}/providers/Microsoft.Insights/dataCollectionRuleAssociations/{associationName}"}  # type: ignore


    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self,
        resource_uri: str,
        association_name: str,
        **kwargs: Any
    ) -> None:
        """Deletes an association.

        Deletes an association.

        :param resource_uri: The identifier of the resource.
        :type resource_uri: str
        :param association_name: The name of the association. The name is case insensitive.
        :type association_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-04-01"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[None]

        
        request = build_delete_request(
            resource_uri=resource_uri,
            association_name=association_name,
            api_version=api_version,
            template_url=self.delete.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponseCommonV2, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': "/{resourceUri}/providers/Microsoft.Insights/dataCollectionRuleAssociations/{associationName}"}  # type: ignore

