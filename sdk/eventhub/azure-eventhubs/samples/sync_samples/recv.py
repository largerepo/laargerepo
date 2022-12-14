#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

"""
An example to show receiving events from an Event Hub partition.
"""
import os
from azure.eventhub import EventPosition, EventHubConsumerClient

CONNECTION_STR = os.environ["EVENT_HUB_CONN_STR"]
EVENT_HUB = os.environ['EVENT_HUB_NAME']

EVENT_POSITION = EventPosition("-1")
PARTITION = "0"

total = 0


def do_operation(event):
    # do some operations on the event, avoid time-consuming ops
    pass


def on_partition_initialize(partition_context):
    # put your code here
    print("Partition: {} has been intialized".format(partition_context.partition_id))


def on_partition_close(partition_context, reason):
    # put your code here
    print("Partition: {} has been closed, reason for closing: {}".format(partition_context.partition_id,
                                                                         reason))


def on_error(partition_context, error):
    # put your code here
    print("Partition: {} met an exception during receiving: {}".format(partition_context.partition_id,
                                                                       error))


def on_events(partition_context, events):
    # put your code here
    global total

    print("received events: {} from partition: {}".format(len(events), partition_context.partition_id))
    total += len(events)
    for event in events:
        do_operation(event)


if __name__ == '__main__':
    consumer_client = EventHubConsumerClient.from_connection_string(
        conn_str=CONNECTION_STR,
        event_hub_path=EVENT_HUB,
    )

    try:
        with consumer_client:
            consumer_client.receive(on_events=on_events, consumer_group='$Default',
                                    on_partition_initialize=on_partition_initialize,
                                    on_partition_close=on_partition_close,
                                    on_error=on_error)
            # Receive with owner level:
            # consumer_client.receive(on_events=on_events, consumer_group='$Default', owner_level=1)
    except KeyboardInterrupt:
        print('Stop receiving.')
