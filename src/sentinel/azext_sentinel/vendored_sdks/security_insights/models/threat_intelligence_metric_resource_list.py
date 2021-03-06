# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ThreatIntelligenceMetricResourceList(Model):
    """List of all the threat intelligence metric resource.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. Array of threat intelligence metrics resource.
    :type value:
     list[~securityinsights.models.ThreatIntelligenceMetricResource]
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ThreatIntelligenceMetricResource]'},
    }

    def __init__(self, **kwargs):
        super(ThreatIntelligenceMetricResourceList, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
