# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models as _models
from ...operations._conversation_analysis_operations import build_analyze_conversations_request

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ConversationAnalysisOperations:
    """ConversationAnalysisOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.ai.language.questionanswering.models
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
    async def analyze_conversations(
        self,
        conversation_analysis_input: "_models.ConversationAnalysisInput",
        *,
        project_name: str,
        deployment_name: str,
        **kwargs: Any
    ) -> "_models.ConversationAnalysisResult":
        """Analyzes the input conversation.

        :param conversation_analysis_input: Post body of the request.
        :type conversation_analysis_input:
         ~azure.ai.language.questionanswering.models.ConversationAnalysisInput
        :keyword project_name: The project name.
        :paramtype project_name: str
        :keyword deployment_name: The deployment name/deployed version.
        :paramtype deployment_name: str
        :return: ConversationAnalysisResult
        :rtype: ~azure.ai.language.questionanswering.models.ConversationAnalysisResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ConversationAnalysisResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        json = self._serialize.body(conversation_analysis_input, 'ConversationAnalysisInput')

        request = build_analyze_conversations_request(
            content_type=content_type,
            project_name=project_name,
            deployment_name=deployment_name,
            json=json,
            template_url=self.analyze_conversations.metadata['url'],
        )
        path_format_arguments = {
            "Endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('ConversationAnalysisResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    analyze_conversations.metadata = {'url': '/:analyze-conversations'}  # type: ignore

