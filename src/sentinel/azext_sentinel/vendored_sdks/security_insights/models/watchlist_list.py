# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class WatchlistList(Model):
    """List all the watchlists.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar next_link: URL to fetch the next set of watchlists.
    :vartype next_link: str
    :param value: Required. Array of watchlist.
    :type value: list[~securityinsights.models.Watchlist]
    """

    _validation = {
        'next_link': {'readonly': True},
        'value': {'required': True},
    }

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'value': {'key': 'value', 'type': '[Watchlist]'},
    }

    def __init__(self, **kwargs):
        super(WatchlistList, self).__init__(**kwargs)
        self.next_link = None
        self.value = kwargs.get('value', None)