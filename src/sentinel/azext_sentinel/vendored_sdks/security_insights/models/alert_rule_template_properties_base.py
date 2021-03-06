# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AlertRuleTemplatePropertiesBase(Model):
    """Base alert rule template property bag.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param alert_rules_created_by_template_count: the number of alert rules
     that were created by this template
    :type alert_rules_created_by_template_count: int
    :ivar created_date_utc: The time that this alert rule template has been
     added.
    :vartype created_date_utc: datetime
    :param description: The description of the alert rule template.
    :type description: str
    :param display_name: The display name for alert rule template.
    :type display_name: str
    :param required_data_connectors: The required data sources for this
     template
    :type required_data_connectors:
     list[~securityinsights.models.AlertRuleTemplateDataSource]
    :param status: The alert rule template status. Possible values include:
     'Installed', 'Available', 'NotAvailable'
    :type status: str or ~securityinsights.models.TemplateStatus
    """

    _validation = {
        'created_date_utc': {'readonly': True},
    }

    _attribute_map = {
        'alert_rules_created_by_template_count': {'key': 'alertRulesCreatedByTemplateCount', 'type': 'int'},
        'created_date_utc': {'key': 'createdDateUTC', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'required_data_connectors': {'key': 'requiredDataConnectors', 'type': '[AlertRuleTemplateDataSource]'},
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AlertRuleTemplatePropertiesBase, self).__init__(**kwargs)
        self.alert_rules_created_by_template_count = kwargs.get('alert_rules_created_by_template_count', None)
        self.created_date_utc = None
        self.description = kwargs.get('description', None)
        self.display_name = kwargs.get('display_name', None)
        self.required_data_connectors = kwargs.get('required_data_connectors', None)
        self.status = kwargs.get('status', None)
