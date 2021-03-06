# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BookmarkExpandParameters(Model):
    """The parameters required to execute an expand operation on the given
    bookmark.

    :param end_time: The end date filter, so the only expansion results
     returned are before this date.
    :type end_time: datetime
    :param expansion_id: The Id of the expansion to perform.
    :type expansion_id: str
    :param start_time: The start date filter, so the only expansion results
     returned are after this date.
    :type start_time: datetime
    """

    _attribute_map = {
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'expansion_id': {'key': 'expansionId', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
    }

    def __init__(self, *, end_time=None, expansion_id: str=None, start_time=None, **kwargs) -> None:
        super(BookmarkExpandParameters, self).__init__(**kwargs)
        self.end_time = end_time
        self.expansion_id = expansion_id
        self.start_time = start_time
