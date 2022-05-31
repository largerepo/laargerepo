# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar, Union

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._gateway_route_configs_operations import build_create_or_update_request_initial, build_delete_request_initial, build_get_request, build_list_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class GatewayRouteConfigsOperations:
    """GatewayRouteConfigsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.appplatform.v2022_03_01_preview.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        service_name: str,
        gateway_name: str,
        route_config_name: str,
        **kwargs: Any
    ) -> "_models.GatewayRouteConfigResource":
        """Get the Spring Cloud Gateway route configs.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :param service_name: The name of the Service resource.
        :type service_name: str
        :param gateway_name: The name of Spring Cloud Gateway.
        :type gateway_name: str
        :param route_config_name: The name of the Spring Cloud Gateway route config.
        :type route_config_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GatewayRouteConfigResource, or the result of cls(response)
        :rtype: ~azure.mgmt.appplatform.v2022_03_01_preview.models.GatewayRouteConfigResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.GatewayRouteConfigResource"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2022-03-01-preview")  # type: str

        
        request = build_get_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            service_name=service_name,
            gateway_name=gateway_name,
            route_config_name=route_config_name,
            api_version=api_version,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('GatewayRouteConfigResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppPlatform/Spring/{serviceName}/gateways/{gatewayName}/routeConfigs/{routeConfigName}"}  # type: ignore


    async def _create_or_update_initial(
        self,
        resource_group_name: str,
        service_name: str,
        gateway_name: str,
        route_config_name: str,
        gateway_route_config_resource: "_models.GatewayRouteConfigResource",
        **kwargs: Any
    ) -> "_models.GatewayRouteConfigResource":
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.GatewayRouteConfigResource"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2022-03-01-preview")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(gateway_route_config_resource, 'GatewayRouteConfigResource')

        request = build_create_or_update_request_initial(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            service_name=service_name,
            gateway_name=gateway_name,
            route_config_name=route_config_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self._create_or_update_initial.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('GatewayRouteConfigResource', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('GatewayRouteConfigResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _create_or_update_initial.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppPlatform/Spring/{serviceName}/gateways/{gatewayName}/routeConfigs/{routeConfigName}"}  # type: ignore


    @distributed_trace_async
    async def begin_create_or_update(
        self,
        resource_group_name: str,
        service_name: str,
        gateway_name: str,
        route_config_name: str,
        gateway_route_config_resource: "_models.GatewayRouteConfigResource",
        **kwargs: Any
    ) -> AsyncLROPoller["_models.GatewayRouteConfigResource"]:
        """Create the default Spring Cloud Gateway route configs or update the existing Spring Cloud
        Gateway route configs.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :param service_name: The name of the Service resource.
        :type service_name: str
        :param gateway_name: The name of Spring Cloud Gateway.
        :type gateway_name: str
        :param route_config_name: The name of the Spring Cloud Gateway route config.
        :type route_config_name: str
        :param gateway_route_config_resource: The Spring Cloud Gateway route config for the create or
         update operation.
        :type gateway_route_config_resource:
         ~azure.mgmt.appplatform.v2022_03_01_preview.models.GatewayRouteConfigResource
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either GatewayRouteConfigResource or the
         result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.appplatform.v2022_03_01_preview.models.GatewayRouteConfigResource]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2022-03-01-preview")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.GatewayRouteConfigResource"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._create_or_update_initial(
                resource_group_name=resource_group_name,
                service_name=service_name,
                gateway_name=gateway_name,
                route_config_name=route_config_name,
                gateway_route_config_resource=gateway_route_config_resource,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x,y,z: x,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize('GatewayRouteConfigResource', pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized


        if polling is True: polling_method = AsyncARMPolling(lro_delay, lro_options={'final-state-via': 'azure-async-operation'}, **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_create_or_update.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppPlatform/Spring/{serviceName}/gateways/{gatewayName}/routeConfigs/{routeConfigName}"}  # type: ignore

    async def _delete_initial(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        service_name: str,
        gateway_name: str,
        route_config_name: str,
        **kwargs: Any
    ) -> None:
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2022-03-01-preview")  # type: str

        
        request = build_delete_request_initial(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            service_name=service_name,
            gateway_name=gateway_name,
            route_config_name=route_config_name,
            api_version=api_version,
            template_url=self._delete_initial.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _delete_initial.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppPlatform/Spring/{serviceName}/gateways/{gatewayName}/routeConfigs/{routeConfigName}"}  # type: ignore


    @distributed_trace_async
    async def begin_delete(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        service_name: str,
        gateway_name: str,
        route_config_name: str,
        **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Delete the Spring Cloud Gateway route config.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :param service_name: The name of the Service resource.
        :type service_name: str
        :param gateway_name: The name of Spring Cloud Gateway.
        :type gateway_name: str
        :param route_config_name: The name of the Spring Cloud Gateway route config.
        :type route_config_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2022-03-01-preview")  # type: str
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._delete_initial(
                resource_group_name=resource_group_name,
                service_name=service_name,
                gateway_name=gateway_name,
                route_config_name=route_config_name,
                api_version=api_version,
                cls=lambda x,y,z: x,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})


        if polling is True: polling_method = AsyncARMPolling(lro_delay, lro_options={'final-state-via': 'azure-async-operation'}, **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_delete.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppPlatform/Spring/{serviceName}/gateways/{gatewayName}/routeConfigs/{routeConfigName}"}  # type: ignore

    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        service_name: str,
        gateway_name: str,
        **kwargs: Any
    ) -> AsyncIterable["_models.GatewayRouteConfigResourceCollection"]:
        """Handle requests to list all Spring Cloud Gateway route configs.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :param service_name: The name of the Service resource.
        :type service_name: str
        :param gateway_name: The name of Spring Cloud Gateway.
        :type gateway_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either GatewayRouteConfigResourceCollection or the result
         of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.appplatform.v2022_03_01_preview.models.GatewayRouteConfigResourceCollection]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2022-03-01-preview")  # type: str

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.GatewayRouteConfigResourceCollection"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    service_name=service_name,
                    gateway_name=gateway_name,
                    api_version=api_version,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    service_name=service_name,
                    gateway_name=gateway_name,
                    api_version=api_version,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("GatewayRouteConfigResourceCollection", pipeline_response)
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
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppPlatform/Spring/{serviceName}/gateways/{gatewayName}/routeConfigs"}  # type: ignore
