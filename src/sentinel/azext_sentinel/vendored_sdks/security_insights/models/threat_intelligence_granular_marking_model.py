# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ThreatIntelligenceGranularMarkingModel(Model):
    """Describes threat granular marking model entity.

    :param language: Language granular marking model
    :type language: str
    :param marking_ref: marking reference granular marking model
    :type marking_ref: int
    :param selectors: granular marking model selectors
    :type selectors: list[str]
    """

    _attribute_map = {
        'language': {'key': 'language', 'type': 'str'},
        'marking_ref': {'key': 'markingRef', 'type': 'int'},
        'selectors': {'key': 'selectors', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(ThreatIntelligenceGranularMarkingModel, self).__init__(**kwargs)
        self.language = kwargs.get('language', None)
        self.marking_ref = kwargs.get('marking_ref', None)
        self.selectors = kwargs.get('selectors', None)
