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

from .resource import Resource


class WorkflowRunActionRepetitionDefinition(Resource):
    """The workflow run action repetition definition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The resource id.
    :vartype id: str
    :ivar name: Gets the resource name.
    :vartype name: str
    :ivar type: Gets the resource type.
    :vartype type: str
    :param location: The resource location.
    :type location: str
    :param tags: The resource tags.
    :type tags: dict[str, str]
    :param start_time: The start time of the workflow scope repetition.
    :type start_time: datetime
    :param end_time: The end time of the workflow scope repetition.
    :type end_time: datetime
    :param correlation: The correlation properties.
    :type correlation: ~azure.mgmt.logic.models.RunActionCorrelation
    :param status: The status of the workflow scope repetition. Possible
     values include: 'NotSpecified', 'Paused', 'Running', 'Waiting',
     'Succeeded', 'Skipped', 'Suspended', 'Cancelled', 'Failed', 'Faulted',
     'TimedOut', 'Aborted', 'Ignored'
    :type status: str or ~azure.mgmt.logic.models.WorkflowStatus
    :param code: The workflow scope repetition code.
    :type code: str
    :param error:
    :type error: object
    :ivar tracking_id: Gets the tracking id.
    :vartype tracking_id: str
    :ivar inputs: Gets the inputs.
    :vartype inputs: object
    :ivar inputs_link: Gets the link to inputs.
    :vartype inputs_link: ~azure.mgmt.logic.models.ContentLink
    :ivar outputs: Gets the outputs.
    :vartype outputs: object
    :ivar outputs_link: Gets the link to outputs.
    :vartype outputs_link: ~azure.mgmt.logic.models.ContentLink
    :ivar tracked_properties: Gets the tracked properties.
    :vartype tracked_properties: object
    :param retry_history: Gets the retry histories.
    :type retry_history: list[~azure.mgmt.logic.models.RetryHistory]
    :param iteration_count:
    :type iteration_count: int
    :param repetition_indexes: The repetition indexes.
    :type repetition_indexes: list[~azure.mgmt.logic.models.RepetitionIndex]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'tracking_id': {'readonly': True},
        'inputs': {'readonly': True},
        'inputs_link': {'readonly': True},
        'outputs': {'readonly': True},
        'outputs_link': {'readonly': True},
        'tracked_properties': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'start_time': {'key': 'properties.startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'properties.endTime', 'type': 'iso-8601'},
        'correlation': {'key': 'properties.correlation', 'type': 'RunActionCorrelation'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'code': {'key': 'properties.code', 'type': 'str'},
        'error': {'key': 'properties.error', 'type': 'object'},
        'tracking_id': {'key': 'properties.trackingId', 'type': 'str'},
        'inputs': {'key': 'properties.inputs', 'type': 'object'},
        'inputs_link': {'key': 'properties.inputsLink', 'type': 'ContentLink'},
        'outputs': {'key': 'properties.outputs', 'type': 'object'},
        'outputs_link': {'key': 'properties.outputsLink', 'type': 'ContentLink'},
        'tracked_properties': {'key': 'properties.trackedProperties', 'type': 'object'},
        'retry_history': {'key': 'properties.retryHistory', 'type': '[RetryHistory]'},
        'iteration_count': {'key': 'properties.iterationCount', 'type': 'int'},
        'repetition_indexes': {'key': 'properties.repetitionIndexes', 'type': '[RepetitionIndex]'},
    }

    def __init__(self, **kwargs):
        super(WorkflowRunActionRepetitionDefinition, self).__init__(**kwargs)
        self.start_time = kwargs.get('start_time', None)
        self.end_time = kwargs.get('end_time', None)
        self.correlation = kwargs.get('correlation', None)
        self.status = kwargs.get('status', None)
        self.code = kwargs.get('code', None)
        self.error = kwargs.get('error', None)
        self.tracking_id = None
        self.inputs = None
        self.inputs_link = None
        self.outputs = None
        self.outputs_link = None
        self.tracked_properties = None
        self.retry_history = kwargs.get('retry_history', None)
        self.iteration_count = kwargs.get('iteration_count', None)
        self.repetition_indexes = kwargs.get('repetition_indexes', None)
