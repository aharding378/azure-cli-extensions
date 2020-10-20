# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ThreatIntelligenceResourceList(Model):
    """List of all the threat intelligence entities.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar next_link: URL to fetch the next set of entities.
    :vartype next_link: str
    :param value: Required. Array of threat intelligence entities.
    :type value: list[~securityinsights.models.ThreatIntelligenceResource]
    """

    _validation = {
        'next_link': {'readonly': True},
        'value': {'required': True},
    }

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'value': {'key': 'value', 'type': '[ThreatIntelligenceResource]'},
    }

    def __init__(self, *, value, **kwargs) -> None:
        super(ThreatIntelligenceResourceList, self).__init__(**kwargs)
        self.next_link = None
        self.value = value
