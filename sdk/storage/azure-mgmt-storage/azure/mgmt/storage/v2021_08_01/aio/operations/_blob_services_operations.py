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
from ...operations._blob_services_operations import build_get_service_properties_request, build_list_request, build_set_service_properties_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class BlobServicesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.storage.v2021_08_01.aio.StorageManagementClient`'s
        :attr:`blob_services` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")


    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        account_name: str,
        **kwargs: Any
    ) -> AsyncIterable[_models.BlobServiceItems]:
        """List blob services of storage account. It returns a collection of one object named default.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only.
        :type account_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either BlobServiceItems or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.storage.v2021_08_01.models.BlobServiceItems]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-08-01"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.BlobServiceItems]

        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    resource_group_name=resource_group_name,
                    account_name=account_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=self.list.metadata['url'],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                
                request = build_list_request(
                    resource_group_name=resource_group_name,
                    account_name=account_name,
                    subscription_id=self._config.subscription_id,
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
            deserialized = self._deserialize("BlobServiceItems", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, AsyncList(list_of_elem)

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
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices"}  # type: ignore

    @distributed_trace_async
    async def set_service_properties(
        self,
        resource_group_name: str,
        account_name: str,
        parameters: _models.BlobServiceProperties,
        **kwargs: Any
    ) -> _models.BlobServiceProperties:
        """Sets the properties of a storage account’s Blob service, including properties for Storage
        Analytics and CORS (Cross-Origin Resource Sharing) rules.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only.
        :type account_name: str
        :param parameters: The properties of a storage account’s Blob service, including properties for
         Storage Analytics and CORS (Cross-Origin Resource Sharing) rules.
        :type parameters: ~azure.mgmt.storage.v2021_08_01.models.BlobServiceProperties
        :keyword blob_services_name: The name of the blob Service within the specified storage account.
         Blob Service Name must be 'default'. Default value is "default". Note that overriding this
         default value may result in unsupported behavior.
        :paramtype blob_services_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: BlobServiceProperties, or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2021_08_01.models.BlobServiceProperties
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-08-01"))  # type: str
        blob_services_name = kwargs.pop('blob_services_name', "default")  # type: str
        content_type = kwargs.pop('content_type', _headers.pop('Content-Type', "application/json"))  # type: Optional[str]
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.BlobServiceProperties]

        _json = self._serialize.body(parameters, 'BlobServiceProperties')

        request = build_set_service_properties_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            blob_services_name=blob_services_name,
            content_type=content_type,
            json=_json,
            template_url=self.set_service_properties.metadata['url'],
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
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('BlobServiceProperties', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    set_service_properties.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/{BlobServicesName}"}  # type: ignore


    @distributed_trace_async
    async def get_service_properties(
        self,
        resource_group_name: str,
        account_name: str,
        **kwargs: Any
    ) -> _models.BlobServiceProperties:
        """Gets the properties of a storage account’s Blob service, including properties for Storage
        Analytics and CORS (Cross-Origin Resource Sharing) rules.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only.
        :type account_name: str
        :keyword blob_services_name: The name of the blob Service within the specified storage account.
         Blob Service Name must be 'default'. Default value is "default". Note that overriding this
         default value may result in unsupported behavior.
        :paramtype blob_services_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: BlobServiceProperties, or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2021_08_01.models.BlobServiceProperties
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-08-01"))  # type: str
        blob_services_name = kwargs.pop('blob_services_name', "default")  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.BlobServiceProperties]

        
        request = build_get_service_properties_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            blob_services_name=blob_services_name,
            template_url=self.get_service_properties.metadata['url'],
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
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('BlobServiceProperties', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_service_properties.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/{BlobServicesName}"}  # type: ignore

