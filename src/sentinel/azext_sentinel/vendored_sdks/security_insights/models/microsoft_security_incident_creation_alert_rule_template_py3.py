# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .alert_rule_template_py3 import AlertRuleTemplate


class MicrosoftSecurityIncidentCreationAlertRuleTemplate(AlertRuleTemplate):
    """Represents MicrosoftSecurityIncidentCreation rule template.

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
    :param alert_rules_created_by_template_count: Required. the number of
     alert rules that were created by this template
    :type alert_rules_created_by_template_count: int
    :ivar created_date_utc: Required. The time that this alert rule template
     has been added.
    :vartype created_date_utc: datetime
    :param description: Required. The description of the alert rule template.
    :type description: str
    :param display_name: Required. The display name for alert rule template.
    :type display_name: str
    :param required_data_connectors: The required data sources for this
     template
    :type required_data_connectors:
     list[~securityinsights.models.AlertRuleTemplateDataSource]
    :param status: Required. The alert rule template status. Possible values
     include: 'Installed', 'Available', 'NotAvailable'
    :type status: str or ~securityinsights.models.TemplateStatus
    :param display_names_filter: the alerts' displayNames on which the cases
     will be generated
    :type display_names_filter: list[str]
    :param display_names_exclude_filter: the alerts' displayNames on which the
     cases will not be generated
    :type display_names_exclude_filter: list[str]
    :param product_filter: Required. The alerts' productName on which the
     cases will be generated. Possible values include: 'Microsoft Cloud App
     Security', 'Azure Security Center', 'Azure Advanced Threat Protection',
     'Azure Active Directory Identity Protection', 'Azure Security Center for
     IoT', 'Office 365 Advanced Threat Protection', 'Microsoft Defender
     Advanced Threat Protection'
    :type product_filter: str or
     ~securityinsights.models.MicrosoftSecurityProductName
    :param severities_filter: the alerts' severities on which the cases will
     be generated
    :type severities_filter: list[str or
     ~securityinsights.models.AlertSeverity]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'kind': {'required': True},
        'alert_rules_created_by_template_count': {'required': True},
        'created_date_utc': {'required': True, 'readonly': True},
        'description': {'required': True},
        'display_name': {'required': True},
        'status': {'required': True},
        'product_filter': {'required': True},
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
        'display_names_filter': {'key': 'properties.displayNamesFilter', 'type': '[str]'},
        'display_names_exclude_filter': {'key': 'properties.displayNamesExcludeFilter', 'type': '[str]'},
        'product_filter': {'key': 'properties.productFilter', 'type': 'str'},
        'severities_filter': {'key': 'properties.severitiesFilter', 'type': '[str]'},
    }

    def __init__(self, *, alert_rules_created_by_template_count: int, description: str, display_name: str, status, product_filter, required_data_connectors=None, display_names_filter=None, display_names_exclude_filter=None, severities_filter=None, **kwargs) -> None:
        super(MicrosoftSecurityIncidentCreationAlertRuleTemplate, self).__init__(**kwargs)
        self.alert_rules_created_by_template_count = alert_rules_created_by_template_count
        self.created_date_utc = None
        self.description = description
        self.display_name = display_name
        self.required_data_connectors = required_data_connectors
        self.status = status
        self.display_names_filter = display_names_filter
        self.display_names_exclude_filter = display_names_exclude_filter
        self.product_filter = product_filter
        self.severities_filter = severities_filter
        self.kind = 'MicrosoftSecurityIncidentCreation'
