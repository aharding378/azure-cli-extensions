# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SettingList(Model):
    """List of all the settings.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. Array of settings.
    :type value: list[~securityinsights.models.Settings]
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Settings]'},
    }

    def __init__(self, **kwargs):
        super(SettingList, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
