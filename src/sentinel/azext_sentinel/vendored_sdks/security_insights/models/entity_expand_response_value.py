# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EntityExpandResponseValue(Model):
    """The expansion result values.

    :param entities: Array of the expansion result entities.
    :type entities: list[~securityinsights.models.Entity]
    """

    _attribute_map = {
        'entities': {'key': 'entities', 'type': '[Entity]'},
    }

    def __init__(self, **kwargs):
        super(EntityExpandResponseValue, self).__init__(**kwargs)
        self.entities = kwargs.get('entities', None)