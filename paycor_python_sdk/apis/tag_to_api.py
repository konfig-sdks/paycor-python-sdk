import typing_extensions

from paycor_python_sdk.apis.tags import TagValues
from paycor_python_sdk.apis.tags.employees_api import EmployeesApi
from paycor_python_sdk.apis.tags.employee_direct_deposits_api import EmployeeDirectDepositsApi
from paycor_python_sdk.apis.tags.employee_taxes_api import EmployeeTaxesApi
from paycor_python_sdk.apis.tags.legal_entity_work_locations_api import LegalEntityWorkLocationsApi
from paycor_python_sdk.apis.tags.persons_api import PersonsApi
from paycor_python_sdk.apis.tags.employee_deductions_api import EmployeeDeductionsApi
from paycor_python_sdk.apis.tags.employee_earnings_api import EmployeeEarningsApi
from paycor_python_sdk.apis.tags.employee_pay_stubs_api import EmployeePayStubsApi
from paycor_python_sdk.apis.tags.employee_legacy_perform_time_schedules_api import EmployeeLegacyPerformTimeSchedulesApi
from paycor_python_sdk.apis.tags.legal_entity_departments_api import LegalEntityDepartmentsApi
from paycor_python_sdk.apis.tags.applicant_tracking_system_api import ApplicantTrackingSystemApi
from paycor_python_sdk.apis.tags.employee_certifications_api import EmployeeCertificationsApi
from paycor_python_sdk.apis.tags.employee_pay_rates_api import EmployeePayRatesApi
from paycor_python_sdk.apis.tags.time_off_requests_api import TimeOffRequestsApi
from paycor_python_sdk.apis.tags.labor_codes_api import LaborCodesApi
from paycor_python_sdk.apis.tags.tenants_api import TenantsApi
from paycor_python_sdk.apis.tags.employee_custom_fields_api import EmployeeCustomFieldsApi
from paycor_python_sdk.apis.tags.employee_documents_api import EmployeeDocumentsApi
from paycor_python_sdk.apis.tags.employee_payroll_hours_api import EmployeePayrollHoursApi
from paycor_python_sdk.apis.tags.employee_i9_verification_api import EmployeeI9VerificationApi
from paycor_python_sdk.apis.tags.employee_onboarding_api import EmployeeOnboardingApi
from paycor_python_sdk.apis.tags.employee_time_card_punches_api import EmployeeTimeCardPunchesApi
from paycor_python_sdk.apis.tags.employee_time_off_accruals_api import EmployeeTimeOffAccrualsApi
from paycor_python_sdk.apis.tags.legal_entities_api import LegalEntitiesApi
from paycor_python_sdk.apis.tags.legal_entity_certifications_api import LegalEntityCertificationsApi
from paycor_python_sdk.apis.tags.employee_emergency_contact_api import EmployeeEmergencyContactApi
from paycor_python_sdk.apis.tags.employee_pay_schedule_api import EmployeePayScheduleApi
from paycor_python_sdk.apis.tags.general_ledger_api import GeneralLedgerApi
from paycor_python_sdk.apis.tags.general_ledger_job_costing_api import GeneralLedgerJobCostingApi
from paycor_python_sdk.apis.tags.labor_categories_api import LaborCategoriesApi
from paycor_python_sdk.apis.tags.legal_entity_deductions_api import LegalEntityDeductionsApi
from paycor_python_sdk.apis.tags.legal_entity_earnings_api import LegalEntityEarningsApi
from paycor_python_sdk.apis.tags.legal_entity_job_titles_api import LegalEntityJobTitlesApi
from paycor_python_sdk.apis.tags.legal_entity_pay_data_api import LegalEntityPayDataApi
from paycor_python_sdk.apis.tags.legal_entity_pay_groups_api import LegalEntityPayGroupsApi
from paycor_python_sdk.apis.tags.legal_entity_payroll_processing_data_api import LegalEntityPayrollProcessingDataApi
from paycor_python_sdk.apis.tags.legal_entity_pay_schedule_api import LegalEntityPayScheduleApi
from paycor_python_sdk.apis.tags.legal_entity_activity_types_api import LegalEntityActivityTypesApi
from paycor_python_sdk.apis.tags.legal_entity_schedule_groups_api import LegalEntityScheduleGroupsApi
from paycor_python_sdk.apis.tags.legal_entity_services_api import LegalEntityServicesApi
from paycor_python_sdk.apis.tags.legal_entity_status_reason_api import LegalEntityStatusReasonApi
from paycor_python_sdk.apis.tags.legal_entity_taxes_api import LegalEntityTaxesApi
from paycor_python_sdk.apis.tags.legal_entity_time_off_types_api import LegalEntityTimeOffTypesApi
from paycor_python_sdk.apis.tags.legal_entity_work_sites_api import LegalEntityWorkSitesApi
from paycor_python_sdk.apis.tags.events_api import EventsApi
from paycor_python_sdk.apis.tags.legal_entity_time_data_api import LegalEntityTimeDataApi
from paycor_python_sdk.apis.tags.job_titles_api import JobTitlesApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.EMPLOYEES: EmployeesApi,
        TagValues.EMPLOYEE_DIRECT_DEPOSITS: EmployeeDirectDepositsApi,
        TagValues.EMPLOYEE_TAXES: EmployeeTaxesApi,
        TagValues.LEGAL_ENTITY_WORK_LOCATIONS: LegalEntityWorkLocationsApi,
        TagValues.PERSONS: PersonsApi,
        TagValues.EMPLOYEE_DEDUCTIONS: EmployeeDeductionsApi,
        TagValues.EMPLOYEE_EARNINGS: EmployeeEarningsApi,
        TagValues.EMPLOYEE_PAY_STUBS: EmployeePayStubsApi,
        TagValues.EMPLOYEE_LEGACY___PERFORM_TIME_SCHEDULES: EmployeeLegacyPerformTimeSchedulesApi,
        TagValues.LEGAL_ENTITY_DEPARTMENTS: LegalEntityDepartmentsApi,
        TagValues.APPLICANT_TRACKING_SYSTEM: ApplicantTrackingSystemApi,
        TagValues.EMPLOYEE_CERTIFICATIONS: EmployeeCertificationsApi,
        TagValues.EMPLOYEE_PAY_RATES: EmployeePayRatesApi,
        TagValues.TIME_OFF_REQUESTS: TimeOffRequestsApi,
        TagValues.LABOR_CODES: LaborCodesApi,
        TagValues.TENANTS: TenantsApi,
        TagValues.EMPLOYEE_CUSTOM_FIELDS: EmployeeCustomFieldsApi,
        TagValues.EMPLOYEE_DOCUMENTS: EmployeeDocumentsApi,
        TagValues.EMPLOYEE_PAYROLL_HOURS: EmployeePayrollHoursApi,
        TagValues.EMPLOYEE_I9_VERIFICATION: EmployeeI9VerificationApi,
        TagValues.EMPLOYEE_ONBOARDING: EmployeeOnboardingApi,
        TagValues.EMPLOYEE_TIME_CARD_PUNCHES: EmployeeTimeCardPunchesApi,
        TagValues.EMPLOYEE_TIME_OFF_ACCRUALS: EmployeeTimeOffAccrualsApi,
        TagValues.LEGAL_ENTITIES: LegalEntitiesApi,
        TagValues.LEGAL_ENTITY_CERTIFICATIONS: LegalEntityCertificationsApi,
        TagValues.EMPLOYEE_EMERGENCY_CONTACT: EmployeeEmergencyContactApi,
        TagValues.EMPLOYEE_PAY_SCHEDULE: EmployeePayScheduleApi,
        TagValues.GENERAL_LEDGER: GeneralLedgerApi,
        TagValues.GENERAL_LEDGER_JOB_COSTING: GeneralLedgerJobCostingApi,
        TagValues.LABOR_CATEGORIES: LaborCategoriesApi,
        TagValues.LEGAL_ENTITY_DEDUCTIONS: LegalEntityDeductionsApi,
        TagValues.LEGAL_ENTITY_EARNINGS: LegalEntityEarningsApi,
        TagValues.LEGAL_ENTITY_JOB_TITLES: LegalEntityJobTitlesApi,
        TagValues.LEGAL_ENTITY_PAY_DATA: LegalEntityPayDataApi,
        TagValues.LEGAL_ENTITY_PAY_GROUPS: LegalEntityPayGroupsApi,
        TagValues.LEGAL_ENTITY_PAYROLL_PROCESSING_DATA: LegalEntityPayrollProcessingDataApi,
        TagValues.LEGAL_ENTITY_PAY_SCHEDULE: LegalEntityPayScheduleApi,
        TagValues.LEGAL_ENTITY_ACTIVITY_TYPES: LegalEntityActivityTypesApi,
        TagValues.LEGAL_ENTITY_SCHEDULE_GROUPS: LegalEntityScheduleGroupsApi,
        TagValues.LEGAL_ENTITY_SERVICES: LegalEntityServicesApi,
        TagValues.LEGAL_ENTITY_STATUS_REASON: LegalEntityStatusReasonApi,
        TagValues.LEGAL_ENTITY_TAXES: LegalEntityTaxesApi,
        TagValues.LEGAL_ENTITY_TIME_OFF_TYPES: LegalEntityTimeOffTypesApi,
        TagValues.LEGAL_ENTITY_WORK_SITES: LegalEntityWorkSitesApi,
        TagValues.EVENTS: EventsApi,
        TagValues.LEGAL_ENTITY_TIME_DATA: LegalEntityTimeDataApi,
        TagValues.JOB_TITLES: JobTitlesApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.EMPLOYEES: EmployeesApi,
        TagValues.EMPLOYEE_DIRECT_DEPOSITS: EmployeeDirectDepositsApi,
        TagValues.EMPLOYEE_TAXES: EmployeeTaxesApi,
        TagValues.LEGAL_ENTITY_WORK_LOCATIONS: LegalEntityWorkLocationsApi,
        TagValues.PERSONS: PersonsApi,
        TagValues.EMPLOYEE_DEDUCTIONS: EmployeeDeductionsApi,
        TagValues.EMPLOYEE_EARNINGS: EmployeeEarningsApi,
        TagValues.EMPLOYEE_PAY_STUBS: EmployeePayStubsApi,
        TagValues.EMPLOYEE_LEGACY___PERFORM_TIME_SCHEDULES: EmployeeLegacyPerformTimeSchedulesApi,
        TagValues.LEGAL_ENTITY_DEPARTMENTS: LegalEntityDepartmentsApi,
        TagValues.APPLICANT_TRACKING_SYSTEM: ApplicantTrackingSystemApi,
        TagValues.EMPLOYEE_CERTIFICATIONS: EmployeeCertificationsApi,
        TagValues.EMPLOYEE_PAY_RATES: EmployeePayRatesApi,
        TagValues.TIME_OFF_REQUESTS: TimeOffRequestsApi,
        TagValues.LABOR_CODES: LaborCodesApi,
        TagValues.TENANTS: TenantsApi,
        TagValues.EMPLOYEE_CUSTOM_FIELDS: EmployeeCustomFieldsApi,
        TagValues.EMPLOYEE_DOCUMENTS: EmployeeDocumentsApi,
        TagValues.EMPLOYEE_PAYROLL_HOURS: EmployeePayrollHoursApi,
        TagValues.EMPLOYEE_I9_VERIFICATION: EmployeeI9VerificationApi,
        TagValues.EMPLOYEE_ONBOARDING: EmployeeOnboardingApi,
        TagValues.EMPLOYEE_TIME_CARD_PUNCHES: EmployeeTimeCardPunchesApi,
        TagValues.EMPLOYEE_TIME_OFF_ACCRUALS: EmployeeTimeOffAccrualsApi,
        TagValues.LEGAL_ENTITIES: LegalEntitiesApi,
        TagValues.LEGAL_ENTITY_CERTIFICATIONS: LegalEntityCertificationsApi,
        TagValues.EMPLOYEE_EMERGENCY_CONTACT: EmployeeEmergencyContactApi,
        TagValues.EMPLOYEE_PAY_SCHEDULE: EmployeePayScheduleApi,
        TagValues.GENERAL_LEDGER: GeneralLedgerApi,
        TagValues.GENERAL_LEDGER_JOB_COSTING: GeneralLedgerJobCostingApi,
        TagValues.LABOR_CATEGORIES: LaborCategoriesApi,
        TagValues.LEGAL_ENTITY_DEDUCTIONS: LegalEntityDeductionsApi,
        TagValues.LEGAL_ENTITY_EARNINGS: LegalEntityEarningsApi,
        TagValues.LEGAL_ENTITY_JOB_TITLES: LegalEntityJobTitlesApi,
        TagValues.LEGAL_ENTITY_PAY_DATA: LegalEntityPayDataApi,
        TagValues.LEGAL_ENTITY_PAY_GROUPS: LegalEntityPayGroupsApi,
        TagValues.LEGAL_ENTITY_PAYROLL_PROCESSING_DATA: LegalEntityPayrollProcessingDataApi,
        TagValues.LEGAL_ENTITY_PAY_SCHEDULE: LegalEntityPayScheduleApi,
        TagValues.LEGAL_ENTITY_ACTIVITY_TYPES: LegalEntityActivityTypesApi,
        TagValues.LEGAL_ENTITY_SCHEDULE_GROUPS: LegalEntityScheduleGroupsApi,
        TagValues.LEGAL_ENTITY_SERVICES: LegalEntityServicesApi,
        TagValues.LEGAL_ENTITY_STATUS_REASON: LegalEntityStatusReasonApi,
        TagValues.LEGAL_ENTITY_TAXES: LegalEntityTaxesApi,
        TagValues.LEGAL_ENTITY_TIME_OFF_TYPES: LegalEntityTimeOffTypesApi,
        TagValues.LEGAL_ENTITY_WORK_SITES: LegalEntityWorkSitesApi,
        TagValues.EVENTS: EventsApi,
        TagValues.LEGAL_ENTITY_TIME_DATA: LegalEntityTimeDataApi,
        TagValues.JOB_TITLES: JobTitlesApi,
    }
)
