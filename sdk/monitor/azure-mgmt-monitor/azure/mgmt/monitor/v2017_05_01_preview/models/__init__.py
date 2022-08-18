# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import DiagnosticSettingsCategoryResource
from ._models_py3 import DiagnosticSettingsCategoryResourceCollection
from ._models_py3 import DiagnosticSettingsResource
from ._models_py3 import DiagnosticSettingsResourceCollection
from ._models_py3 import ErrorResponse
from ._models_py3 import LocalizableString
from ._models_py3 import LogSettings
from ._models_py3 import MetadataValue
from ._models_py3 import Metric
from ._models_py3 import MetricAvailability
from ._models_py3 import MetricDefinition
from ._models_py3 import MetricDefinitionCollection
from ._models_py3 import MetricSettings
from ._models_py3 import MetricValue
from ._models_py3 import ProxyOnlyResource
from ._models_py3 import Response
from ._models_py3 import RetentionPolicy
from ._models_py3 import SubscriptionDiagnosticSettingsResource
from ._models_py3 import SubscriptionDiagnosticSettingsResourceCollection
from ._models_py3 import SubscriptionLogSettings
from ._models_py3 import SubscriptionProxyOnlyResource
from ._models_py3 import TimeSeriesElement


from ._monitor_management_client_enums import (
    AggregationType,
    CategoryType,
    ResultType,
    Unit,
)
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk
__all__ = [
    'DiagnosticSettingsCategoryResource',
    'DiagnosticSettingsCategoryResourceCollection',
    'DiagnosticSettingsResource',
    'DiagnosticSettingsResourceCollection',
    'ErrorResponse',
    'LocalizableString',
    'LogSettings',
    'MetadataValue',
    'Metric',
    'MetricAvailability',
    'MetricDefinition',
    'MetricDefinitionCollection',
    'MetricSettings',
    'MetricValue',
    'ProxyOnlyResource',
    'Response',
    'RetentionPolicy',
    'SubscriptionDiagnosticSettingsResource',
    'SubscriptionDiagnosticSettingsResourceCollection',
    'SubscriptionLogSettings',
    'SubscriptionProxyOnlyResource',
    'TimeSeriesElement',
    'AggregationType',
    'CategoryType',
    'ResultType',
    'Unit',
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()