# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import DataSource
from ._models_py3 import DataSourceConfiguration
from ._models_py3 import ErrorResponse
from ._models_py3 import EtwEventConfiguration
from ._models_py3 import EtwProviderConfiguration
from ._models_py3 import EventLogConfiguration
from ._models_py3 import GuestDiagnosticSettingsAssociationList
from ._models_py3 import GuestDiagnosticSettingsAssociationResource
from ._models_py3 import GuestDiagnosticSettingsAssociationResourcePatch
from ._models_py3 import GuestDiagnosticSettingsList
from ._models_py3 import GuestDiagnosticSettingsPatchResource
from ._models_py3 import GuestDiagnosticSettingsResource
from ._models_py3 import PerformanceCounterConfiguration
from ._models_py3 import Resource
from ._models_py3 import SinkConfiguration


from ._monitor_management_client_enums import (
    DataSourceKind,
    GuestDiagnosticSettingsOsType,
    SinkConfigurationKind,
)
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk
__all__ = [
    'DataSource',
    'DataSourceConfiguration',
    'ErrorResponse',
    'EtwEventConfiguration',
    'EtwProviderConfiguration',
    'EventLogConfiguration',
    'GuestDiagnosticSettingsAssociationList',
    'GuestDiagnosticSettingsAssociationResource',
    'GuestDiagnosticSettingsAssociationResourcePatch',
    'GuestDiagnosticSettingsList',
    'GuestDiagnosticSettingsPatchResource',
    'GuestDiagnosticSettingsResource',
    'PerformanceCounterConfiguration',
    'Resource',
    'SinkConfiguration',
    'DataSourceKind',
    'GuestDiagnosticSettingsOsType',
    'SinkConfigurationKind',
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()