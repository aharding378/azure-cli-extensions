# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .alert_rule_template import AlertRuleTemplate


class FusionAlertRuleTemplate(AlertRuleTemplate):
    """Represents Fusion alert rule template.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar name: Azure resource name
    :vartype name: str
    :ivar type: Azure resource type
    :vartype type: str
    :param kind: Required. Constant filled by server.
    :type kind: str
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
    :param severity: Required. The severity for alerts created by this alert
     rule. Possible values include: 'High', 'Medium', 'Low', 'Informational'
    :type severity: str or ~securityinsights.models.AlertSeverity
    :param tactics: The tactics of the alert rule template
    :type tactics: list[str or ~securityinsights.models.AttackTactic]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'kind': {'required': True},
        'created_date_utc': {'readonly': True},
        'severity': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'alert_rules_created_by_template_count': {'key': 'properties.alertRulesCreatedByTemplateCount', 'type': 'int'},
        'created_date_utc': {'key': 'properties.createdDateUTC', 'type': 'iso-8601'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'required_data_connectors': {'key': 'properties.requiredDataConnectors', 'type': '[AlertRuleTemplateDataSource]'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'severity': {'key': 'properties.severity', 'type': 'str'},
        'tactics': {'key': 'properties.tactics', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(FusionAlertRuleTemplate, self).__init__(**kwargs)
        self.alert_rules_created_by_template_count = kwargs.get('alert_rules_created_by_template_count', None)
        self.created_date_utc = None
        self.description = kwargs.get('description', None)
        self.display_name = kwargs.get('display_name', None)
        self.required_data_connectors = kwargs.get('required_data_connectors', None)
        self.status = kwargs.get('status', None)
        self.severity = kwargs.get('severity', None)
        self.tactics = kwargs.get('tactics', None)
        self.kind = 'Fusion'
