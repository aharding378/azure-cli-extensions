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

from .proxy_resource_py3 import ProxyResource


class RestorePoint(ProxyResource):
    """Database restore points.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar location: Resource location.
    :vartype location: str
    :ivar restore_point_type: The type of restore point. Possible values
     include: 'CONTINUOUS', 'DISCRETE'
    :vartype restore_point_type: str or
     ~azure.mgmt.sql.models.RestorePointType
    :ivar earliest_restore_date: The earliest time to which this database can
     be restored
    :vartype earliest_restore_date: datetime
    :ivar restore_point_creation_date: The time the backup was taken
    :vartype restore_point_creation_date: datetime
    :ivar restore_point_label: The label of restore point for backup request
     by user
    :vartype restore_point_label: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'readonly': True},
        'restore_point_type': {'readonly': True},
        'earliest_restore_date': {'readonly': True},
        'restore_point_creation_date': {'readonly': True},
        'restore_point_label': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'restore_point_type': {'key': 'properties.restorePointType', 'type': 'RestorePointType'},
        'earliest_restore_date': {'key': 'properties.earliestRestoreDate', 'type': 'iso-8601'},
        'restore_point_creation_date': {'key': 'properties.restorePointCreationDate', 'type': 'iso-8601'},
        'restore_point_label': {'key': 'properties.restorePointLabel', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(RestorePoint, self).__init__(**kwargs)
        self.location = None
        self.restore_point_type = None
        self.earliest_restore_date = None
        self.restore_point_creation_date = None
        self.restore_point_label = None
