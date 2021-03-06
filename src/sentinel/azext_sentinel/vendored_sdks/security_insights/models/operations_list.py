# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class OperationsList(Model):
    """Lists the operations available in the SecurityInsights RP.

    All required parameters must be populated in order to send to Azure.

    :param next_link: URL to fetch the next set of operations.
    :type next_link: str
    :param value: Required. Array of operations
    :type value: list[~securityinsights.models.Operation]
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'value': {'key': 'value', 'type': '[Operation]'},
    }

    def __init__(self, **kwargs):
        super(OperationsList, self).__init__(**kwargs)
        self.next_link = kwargs.get('next_link', None)
        self.value = kwargs.get('value', None)
