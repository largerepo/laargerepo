# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .copy_sink import CopySink


class SqlMISink(CopySink):
    """A copy activity Azure SQL Managed Instance sink.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param write_batch_size: Write batch size. Type: integer (or Expression
     with resultType integer), minimum: 0.
    :type write_batch_size: object
    :param write_batch_timeout: Write batch timeout. Type: string (or
     Expression with resultType string), pattern:
     ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])).
    :type write_batch_timeout: object
    :param sink_retry_count: Sink retry count. Type: integer (or Expression
     with resultType integer).
    :type sink_retry_count: object
    :param sink_retry_wait: Sink retry wait. Type: string (or Expression with
     resultType string), pattern:
     ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])).
    :type sink_retry_wait: object
    :param max_concurrent_connections: The maximum concurrent connection count
     for the sink data store. Type: integer (or Expression with resultType
     integer).
    :type max_concurrent_connections: object
    :param type: Required. Constant filled by server.
    :type type: str
    :param sql_writer_stored_procedure_name: SQL writer stored procedure name.
     Type: string (or Expression with resultType string).
    :type sql_writer_stored_procedure_name: object
    :param sql_writer_table_type: SQL writer table type. Type: string (or
     Expression with resultType string).
    :type sql_writer_table_type: object
    :param pre_copy_script: SQL pre-copy script. Type: string (or Expression
     with resultType string).
    :type pre_copy_script: object
    :param stored_procedure_parameters: SQL stored procedure parameters.
    :type stored_procedure_parameters: dict[str,
     ~azure.mgmt.datafactory.models.StoredProcedureParameter]
    :param stored_procedure_table_type_parameter_name: The stored procedure
     parameter name of the table type. Type: string (or Expression with
     resultType string).
    :type stored_procedure_table_type_parameter_name: object
    :param table_option: The option to handle sink table, such as autoCreate.
     For now only 'autoCreate' value is supported. Type: string (or Expression
     with resultType string).
    :type table_option: object
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'write_batch_size': {'key': 'writeBatchSize', 'type': 'object'},
        'write_batch_timeout': {'key': 'writeBatchTimeout', 'type': 'object'},
        'sink_retry_count': {'key': 'sinkRetryCount', 'type': 'object'},
        'sink_retry_wait': {'key': 'sinkRetryWait', 'type': 'object'},
        'max_concurrent_connections': {'key': 'maxConcurrentConnections', 'type': 'object'},
        'type': {'key': 'type', 'type': 'str'},
        'sql_writer_stored_procedure_name': {'key': 'sqlWriterStoredProcedureName', 'type': 'object'},
        'sql_writer_table_type': {'key': 'sqlWriterTableType', 'type': 'object'},
        'pre_copy_script': {'key': 'preCopyScript', 'type': 'object'},
        'stored_procedure_parameters': {'key': 'storedProcedureParameters', 'type': '{StoredProcedureParameter}'},
        'stored_procedure_table_type_parameter_name': {'key': 'storedProcedureTableTypeParameterName', 'type': 'object'},
        'table_option': {'key': 'tableOption', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(SqlMISink, self).__init__(**kwargs)
        self.sql_writer_stored_procedure_name = kwargs.get('sql_writer_stored_procedure_name', None)
        self.sql_writer_table_type = kwargs.get('sql_writer_table_type', None)
        self.pre_copy_script = kwargs.get('pre_copy_script', None)
        self.stored_procedure_parameters = kwargs.get('stored_procedure_parameters', None)
        self.stored_procedure_table_type_parameter_name = kwargs.get('stored_procedure_table_type_parameter_name', None)
        self.table_option = kwargs.get('table_option', None)
        self.type = 'SqlMISink'
