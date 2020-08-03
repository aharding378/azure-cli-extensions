# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DataConnectorTenantId(Model):
    """Properties data connector on tenant level.

    :param tenant_id: The tenant id to connect to, and get the data from.
    :type tenant_id: str
    """

    _attribute_map = {
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
    }

    def __init__(self, *, tenant_id: str=None, **kwargs) -> None:
        super(DataConnectorTenantId, self).__init__(**kwargs)
        self.tenant_id = tenant_id