# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class IncidentAlertList(Model):
    """List of incident alerts.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. Array of incident alerts.
    :type value: list[~securityinsights.models.SecurityAlert]
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[SecurityAlert]'},
    }

    def __init__(self, **kwargs):
        super(IncidentAlertList, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)