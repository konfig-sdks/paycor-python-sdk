import typing_extensions

from paycor_python_sdk.paths import PathValues
from paycor_python_sdk.apis.paths.v1_legal_entities_legal_entity_id_ats_ats_account_id_jobs import V1LegalEntitiesLegalEntityIdAtsAtsAccountIdJobs
from paycor_python_sdk.apis.paths.v1_legal_entities_legal_entity_id_ats_ats_account_id_jobs_ats_job_id import V1LegalEntitiesLegalEntityIdAtsAtsAccountIdJobsAtsJobId
from paycor_python_sdk.apis.paths.v1_legal_entities_legal_entity_id_ats_accounts import V1LegalEntitiesLegalEntityIdAtsAccounts
from paycor_python_sdk.apis.paths.v1_employees_employee_id_emergencycontact import V1EmployeesEmployeeIdEmergencycontact
from paycor_python_sdk.apis.paths.v1_employees_employee_id_certifications import V1EmployeesEmployeeIdCertifications
from paycor_python_sdk.apis.paths.v1_employees_employee_id_customfields import V1EmployeesEmployeeIdCustomfields
from paycor_python_sdk.apis.paths.v1_employees_employee_id_deductions_employee_deduction_id import V1EmployeesEmployeeIdDeductionsEmployeeDeductionId
from paycor_python_sdk.apis.paths.v1_employees_employee_id_deductions import V1EmployeesEmployeeIdDeductions
from paycor_python_sdk.apis.paths.v1_employees_employee_id_hs_aaccounts import V1EmployeesEmployeeIdHSAaccounts
from paycor_python_sdk.apis.paths.v1_employees_employee_id_direct_deposits import V1EmployeesEmployeeIdDirectDeposits
from paycor_python_sdk.apis.paths.v1_employees_employee_id_direct_deposits_direct_deposit_id import V1EmployeesEmployeeIdDirectDepositsDirectDepositId
from paycor_python_sdk.apis.paths.v1_employees_employee_id_paystub_document_data import V1EmployeesEmployeeIdPaystubDocumentData
from paycor_python_sdk.apis.paths.v1_employees_employee_id_pay_stub_document_document_id import V1EmployeesEmployeeIdPayStubDocumentDocumentId
from paycor_python_sdk.apis.paths.v1_employees_employee_id_earnings_employee_earning_id import V1EmployeesEmployeeIdEarningsEmployeeEarningId
from paycor_python_sdk.apis.paths.v1_employees_employee_id_earnings import V1EmployeesEmployeeIdEarnings
from paycor_python_sdk.apis.paths.v1_legalentities_legal_entity_id_payrollhours import V1LegalentitiesLegalEntityIdPayrollhours
from paycor_python_sdk.apis.paths.v1_employees_employee_id_payrollhours import V1EmployeesEmployeeIdPayrollhours
from paycor_python_sdk.apis.paths.v1_employees_employee_id_i9_verification import V1EmployeesEmployeeIdI9Verification
from paycor_python_sdk.apis.paths.v1_employees_employee_id_payrates import V1EmployeesEmployeeIdPayrates
from paycor_python_sdk.apis.paths.v1_employees_employee_id_payrates_payrate_id import V1EmployeesEmployeeIdPayratesPayrateId
from paycor_python_sdk.apis.paths.v1_employees_employee_id_payschedule import V1EmployeesEmployeeIdPayschedule
from paycor_python_sdk.apis.paths.v1_employees_employee_id_paystubs import V1EmployeesEmployeeIdPaystubs
from paycor_python_sdk.apis.paths.v1_legalentities_legal_entity_id_paystubs import V1LegalentitiesLegalEntityIdPaystubs
from paycor_python_sdk.apis.paths.v1_employees_employee_id_paystubsytd import V1EmployeesEmployeeIdPaystubsytd
from paycor_python_sdk.apis.paths.v1_legalentities_legal_entity_id_paystubsytd import V1LegalentitiesLegalEntityIdPaystubsytd
from paycor_python_sdk.apis.paths.v1_employees_employee_id_schedules import V1EmployeesEmployeeIdSchedules
from paycor_python_sdk.apis.paths.v1_legal_entities_legal_entity_id_schedules import V1LegalEntitiesLegalEntityIdSchedules
from paycor_python_sdk.apis.paths.v1_employees_employee_id_schedules_schedule_id import V1EmployeesEmployeeIdSchedulesScheduleId
from paycor_python_sdk.apis.paths.v1_employees_employee_id import V1EmployeesEmployeeId
from paycor_python_sdk.apis.paths.v1_tenants_tenant_id_employees import V1TenantsTenantIdEmployees
from paycor_python_sdk.apis.paths.v1_legalentities_legal_entity_id_employees import V1LegalentitiesLegalEntityIdEmployees
from paycor_python_sdk.apis.paths.v1_employees import V1Employees
from paycor_python_sdk.apis.paths.v1_employees_employee_id_positionandstatus import V1EmployeesEmployeeIdPositionandstatus
from paycor_python_sdk.apis.paths.v1_employees_employee_id_position import V1EmployeesEmployeeIdPosition
from paycor_python_sdk.apis.paths.v1_employees_employee_id_status import V1EmployeesEmployeeIdStatus
from paycor_python_sdk.apis.paths.v1_employees_employee_id_identifyingdata import V1EmployeesEmployeeIdIdentifyingdata
from paycor_python_sdk.apis.paths.v1_legalentities_legal_entity_id_employees_identifying_data import V1LegalentitiesLegalEntityIdEmployeesIdentifyingData
from paycor_python_sdk.apis.paths.v1_employees_employee_id_paygroup import V1EmployeesEmployeeIdPaygroup
from paycor_python_sdk.apis.paths.v1_employees_onboarding import V1EmployeesOnboarding
from paycor_python_sdk.apis.paths.v1_legalentities_legal_entity_id_onboardingemployees import V1LegalentitiesLegalEntityIdOnboardingemployees
from paycor_python_sdk.apis.paths.v1_employees_employee_id_taxes import V1EmployeesEmployeeIdTaxes
from paycor_python_sdk.apis.paths.v1_employees_taxes_filing_status_tax_code import V1EmployeesTaxesFilingStatusTaxCode
from paycor_python_sdk.apis.paths.v1_employees_taxes_tax_fields_tax_code import V1EmployeesTaxesTaxFieldsTaxCode
from paycor_python_sdk.apis.paths.v1_legal_entities_legal_entity_id_punches import V1LegalEntitiesLegalEntityIdPunches
from paycor_python_sdk.apis.paths.v1_employees_employee_id_punches import V1EmployeesEmployeeIdPunches
from paycor_python_sdk.apis.paths.v1_employees_employee_id_timeoffaccruals import V1EmployeesEmployeeIdTimeoffaccruals
from paycor_python_sdk.apis.paths.v1_legalentities_legal_entity_id_timeoffaccruals import V1LegalentitiesLegalEntityIdTimeoffaccruals
from paycor_python_sdk.apis.paths.v1_employees_employee_id_timeoffrequests import V1EmployeesEmployeeIdTimeoffrequests
from paycor_python_sdk.apis.paths.v1_events_mockevent import V1EventsMockevent
from paycor_python_sdk.apis.paths.v1_generalledger_legalentities_legal_entity_id import V1GeneralledgerLegalentitiesLegalEntityId
from paycor_python_sdk.apis.paths.v1_generalledger_jobcosting_legalentities_legal_entity_id import V1GeneralledgerJobcostingLegalentitiesLegalEntityId
from paycor_python_sdk.apis.paths.v1_legalentities_legal_entity_id_laborcategories import V1LegalentitiesLegalEntityIdLaborcategories
from paycor_python_sdk.apis.paths.v1_legalentities_legal_entity_id_laborcodes import V1LegalentitiesLegalEntityIdLaborcodes
from paycor_python_sdk.apis.paths.v1_legalentities_legal_entity_id import V1LegalentitiesLegalEntityId
from paycor_python_sdk.apis.paths.v1_legalentities_activated_legal_entity_tenant_list import V1LegalentitiesActivatedLegalEntityTenantList
from paycor_python_sdk.apis.paths.v1_legalentities_legal_entity_id_certification_organizations import V1LegalentitiesLegalEntityIdCertificationOrganizations
from paycor_python_sdk.apis.paths.v1_legalentities_legal_entity_id_certifications import V1LegalentitiesLegalEntityIdCertifications
from paycor_python_sdk.apis.paths.v1_legalentities_legal_entity_id_deductions import V1LegalentitiesLegalEntityIdDeductions
from paycor_python_sdk.apis.paths.v1_legalentities_legal_entity_id_departments import V1LegalentitiesLegalEntityIdDepartments
from paycor_python_sdk.apis.paths.v1_legalentities_legal_entity_id_departments_department_id import V1LegalentitiesLegalEntityIdDepartmentsDepartmentId
from paycor_python_sdk.apis.paths.v1_legalentities_legal_entity_id_earnings import V1LegalentitiesLegalEntityIdEarnings
from paycor_python_sdk.apis.paths.v1_legalentities_legal_entity_id_jobtitles import V1LegalentitiesLegalEntityIdJobtitles
from paycor_python_sdk.apis.paths.v1_legalentities_legal_entity_id_paydata import V1LegalentitiesLegalEntityIdPaydata
from paycor_python_sdk.apis.paths.v1_legalentities_legal_entity_id_pay_groups import V1LegalentitiesLegalEntityIdPayGroups
from paycor_python_sdk.apis.paths.v1_legalentities_legal_entity_id_payroll_processing import V1LegalentitiesLegalEntityIdPayrollProcessing
from paycor_python_sdk.apis.paths.v1_legalentities_legal_entity_id_payschedule import V1LegalentitiesLegalEntityIdPayschedule
from paycor_python_sdk.apis.paths.v1_legalentities_legal_entity_id_activitytypes import V1LegalentitiesLegalEntityIdActivitytypes
from paycor_python_sdk.apis.paths.v1_legalentities_legal_entity_id_schedulegroups import V1LegalentitiesLegalEntityIdSchedulegroups
from paycor_python_sdk.apis.paths.v1_legalentities_legal_entity_id_services import V1LegalentitiesLegalEntityIdServices
from paycor_python_sdk.apis.paths.v1_legalentities_legal_entity_id_status_reasons_status_category import V1LegalentitiesLegalEntityIdStatusReasonsStatusCategory
from paycor_python_sdk.apis.paths.v1_legalentities_legal_entity_id_taxes import V1LegalentitiesLegalEntityIdTaxes
from paycor_python_sdk.apis.paths.v1_legalentities_legal_entity_id_timeoffrequests import V1LegalentitiesLegalEntityIdTimeoffrequests
from paycor_python_sdk.apis.paths.v1_legalentities_legal_entity_id_timeoff_requests_timeoff_request_id import V1LegalentitiesLegalEntityIdTimeoffRequestsTimeoffRequestId
from paycor_python_sdk.apis.paths.v1_legalentities_legal_entity_id_timeoff_requestserrorlog_tracking_id import V1LegalentitiesLegalEntityIdTimeoffRequestserrorlogTrackingId
from paycor_python_sdk.apis.paths.v1_legalentities_legal_entity_id_timeofftypes import V1LegalentitiesLegalEntityIdTimeofftypes
from paycor_python_sdk.apis.paths.v1_legalentities_legal_entity_id_worklocations import V1LegalentitiesLegalEntityIdWorklocations
from paycor_python_sdk.apis.paths.v1_legalentities_legal_entity_id_worklocations_work_location_id import V1LegalentitiesLegalEntityIdWorklocationsWorkLocationId
from paycor_python_sdk.apis.paths.v1_legalentities_legal_entity_id_worksites import V1LegalentitiesLegalEntityIdWorksites
from paycor_python_sdk.apis.paths.v1_legal_entities_legal_entity_id_persons import V1LegalEntitiesLegalEntityIdPersons
from paycor_python_sdk.apis.paths.v1_tenants_tenant_id_persons import V1TenantsTenantIdPersons
from paycor_python_sdk.apis.paths.v1_tenants_tenant_id_persons_person_id import V1TenantsTenantIdPersonsPersonId
from paycor_python_sdk.apis.paths.v1_employees_employee_id_person import V1EmployeesEmployeeIdPerson
from paycor_python_sdk.apis.paths.v1_tenants_tenant_id import V1TenantsTenantId
from paycor_python_sdk.apis.paths.v1_tenants_tenant_id_worklocations import V1TenantsTenantIdWorklocations
from paycor_python_sdk.apis.paths.v1_tenants_tenant_id_jobtitles import V1TenantsTenantIdJobtitles

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_LEGAL_ENTITIES_LEGAL_ENTITY_ID_ATS_ATS_ACCOUNT_ID_JOBS: V1LegalEntitiesLegalEntityIdAtsAtsAccountIdJobs,
        PathValues.V1_LEGAL_ENTITIES_LEGAL_ENTITY_ID_ATS_ATS_ACCOUNT_ID_JOBS_ATS_JOB_ID: V1LegalEntitiesLegalEntityIdAtsAtsAccountIdJobsAtsJobId,
        PathValues.V1_LEGAL_ENTITIES_LEGAL_ENTITY_ID_ATS_ACCOUNTS: V1LegalEntitiesLegalEntityIdAtsAccounts,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_EMERGENCYCONTACT: V1EmployeesEmployeeIdEmergencycontact,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_CERTIFICATIONS: V1EmployeesEmployeeIdCertifications,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_CUSTOMFIELDS: V1EmployeesEmployeeIdCustomfields,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_DEDUCTIONS_EMPLOYEE_DEDUCTION_ID: V1EmployeesEmployeeIdDeductionsEmployeeDeductionId,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_DEDUCTIONS: V1EmployeesEmployeeIdDeductions,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_HSAACCOUNTS: V1EmployeesEmployeeIdHSAaccounts,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_DIRECT_DEPOSITS: V1EmployeesEmployeeIdDirectDeposits,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_DIRECT_DEPOSITS_DIRECT_DEPOSIT_ID: V1EmployeesEmployeeIdDirectDepositsDirectDepositId,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_PAYSTUB_DOCUMENT_DATA: V1EmployeesEmployeeIdPaystubDocumentData,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_PAY_STUB_DOCUMENT_DOCUMENT_ID: V1EmployeesEmployeeIdPayStubDocumentDocumentId,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_EARNINGS_EMPLOYEE_EARNING_ID: V1EmployeesEmployeeIdEarningsEmployeeEarningId,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_EARNINGS: V1EmployeesEmployeeIdEarnings,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_PAYROLLHOURS: V1LegalentitiesLegalEntityIdPayrollhours,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_PAYROLLHOURS: V1EmployeesEmployeeIdPayrollhours,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_I9VERIFICATION: V1EmployeesEmployeeIdI9Verification,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_PAYRATES: V1EmployeesEmployeeIdPayrates,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_PAYRATES_PAYRATE_ID: V1EmployeesEmployeeIdPayratesPayrateId,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_PAYSCHEDULE: V1EmployeesEmployeeIdPayschedule,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_PAYSTUBS: V1EmployeesEmployeeIdPaystubs,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_PAYSTUBS: V1LegalentitiesLegalEntityIdPaystubs,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_PAYSTUBSYTD: V1EmployeesEmployeeIdPaystubsytd,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_PAYSTUBSYTD: V1LegalentitiesLegalEntityIdPaystubsytd,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_SCHEDULES: V1EmployeesEmployeeIdSchedules,
        PathValues.V1_LEGAL_ENTITIES_LEGAL_ENTITY_ID_SCHEDULES: V1LegalEntitiesLegalEntityIdSchedules,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_SCHEDULES_SCHEDULE_ID: V1EmployeesEmployeeIdSchedulesScheduleId,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID: V1EmployeesEmployeeId,
        PathValues.V1_TENANTS_TENANT_ID_EMPLOYEES: V1TenantsTenantIdEmployees,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_EMPLOYEES: V1LegalentitiesLegalEntityIdEmployees,
        PathValues.V1_EMPLOYEES: V1Employees,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_POSITIONANDSTATUS: V1EmployeesEmployeeIdPositionandstatus,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_POSITION: V1EmployeesEmployeeIdPosition,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_STATUS: V1EmployeesEmployeeIdStatus,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_IDENTIFYINGDATA: V1EmployeesEmployeeIdIdentifyingdata,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_EMPLOYEES_IDENTIFYING_DATA: V1LegalentitiesLegalEntityIdEmployeesIdentifyingData,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_PAYGROUP: V1EmployeesEmployeeIdPaygroup,
        PathValues.V1_EMPLOYEES_ONBOARDING: V1EmployeesOnboarding,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_ONBOARDINGEMPLOYEES: V1LegalentitiesLegalEntityIdOnboardingemployees,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_TAXES: V1EmployeesEmployeeIdTaxes,
        PathValues.V1_EMPLOYEES_TAXES_FILING_STATUS_TAX_CODE: V1EmployeesTaxesFilingStatusTaxCode,
        PathValues.V1_EMPLOYEES_TAXES_TAX_FIELDS_TAX_CODE: V1EmployeesTaxesTaxFieldsTaxCode,
        PathValues.V1_LEGAL_ENTITIES_LEGAL_ENTITY_ID_PUNCHES: V1LegalEntitiesLegalEntityIdPunches,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_PUNCHES: V1EmployeesEmployeeIdPunches,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_TIMEOFFACCRUALS: V1EmployeesEmployeeIdTimeoffaccruals,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_TIMEOFFACCRUALS: V1LegalentitiesLegalEntityIdTimeoffaccruals,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_TIMEOFFREQUESTS: V1EmployeesEmployeeIdTimeoffrequests,
        PathValues.V1_EVENTS_MOCKEVENT: V1EventsMockevent,
        PathValues.V1_GENERALLEDGER_LEGALENTITIES_LEGAL_ENTITY_ID: V1GeneralledgerLegalentitiesLegalEntityId,
        PathValues.V1_GENERALLEDGER_JOBCOSTING_LEGALENTITIES_LEGAL_ENTITY_ID: V1GeneralledgerJobcostingLegalentitiesLegalEntityId,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_LABORCATEGORIES: V1LegalentitiesLegalEntityIdLaborcategories,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_LABORCODES: V1LegalentitiesLegalEntityIdLaborcodes,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID: V1LegalentitiesLegalEntityId,
        PathValues.V1_LEGALENTITIES_ACTIVATED_LEGAL_ENTITY_TENANT_LIST: V1LegalentitiesActivatedLegalEntityTenantList,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_CERTIFICATION_ORGANIZATIONS: V1LegalentitiesLegalEntityIdCertificationOrganizations,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_CERTIFICATIONS: V1LegalentitiesLegalEntityIdCertifications,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_DEDUCTIONS: V1LegalentitiesLegalEntityIdDeductions,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_DEPARTMENTS: V1LegalentitiesLegalEntityIdDepartments,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_DEPARTMENTS_DEPARTMENT_ID: V1LegalentitiesLegalEntityIdDepartmentsDepartmentId,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_EARNINGS: V1LegalentitiesLegalEntityIdEarnings,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_JOBTITLES: V1LegalentitiesLegalEntityIdJobtitles,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_PAYDATA: V1LegalentitiesLegalEntityIdPaydata,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_PAY_GROUPS: V1LegalentitiesLegalEntityIdPayGroups,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_PAYROLL_PROCESSING: V1LegalentitiesLegalEntityIdPayrollProcessing,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_PAYSCHEDULE: V1LegalentitiesLegalEntityIdPayschedule,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_ACTIVITYTYPES: V1LegalentitiesLegalEntityIdActivitytypes,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_SCHEDULEGROUPS: V1LegalentitiesLegalEntityIdSchedulegroups,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_SERVICES: V1LegalentitiesLegalEntityIdServices,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_STATUS_REASONS_STATUS_CATEGORY: V1LegalentitiesLegalEntityIdStatusReasonsStatusCategory,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_TAXES: V1LegalentitiesLegalEntityIdTaxes,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_TIMEOFFREQUESTS: V1LegalentitiesLegalEntityIdTimeoffrequests,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_TIMEOFF_REQUESTS_TIMEOFF_REQUEST_ID: V1LegalentitiesLegalEntityIdTimeoffRequestsTimeoffRequestId,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_TIMEOFF_REQUESTSERRORLOG_TRACKING_ID: V1LegalentitiesLegalEntityIdTimeoffRequestserrorlogTrackingId,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_TIMEOFFTYPES: V1LegalentitiesLegalEntityIdTimeofftypes,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_WORKLOCATIONS: V1LegalentitiesLegalEntityIdWorklocations,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_WORKLOCATIONS_WORK_LOCATION_ID: V1LegalentitiesLegalEntityIdWorklocationsWorkLocationId,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_WORKSITES: V1LegalentitiesLegalEntityIdWorksites,
        PathValues.V1_LEGAL_ENTITIES_LEGAL_ENTITY_ID_PERSONS: V1LegalEntitiesLegalEntityIdPersons,
        PathValues.V1_TENANTS_TENANT_ID_PERSONS: V1TenantsTenantIdPersons,
        PathValues.V1_TENANTS_TENANT_ID_PERSONS_PERSON_ID: V1TenantsTenantIdPersonsPersonId,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_PERSON: V1EmployeesEmployeeIdPerson,
        PathValues.V1_TENANTS_TENANT_ID: V1TenantsTenantId,
        PathValues.V1_TENANTS_TENANT_ID_WORKLOCATIONS: V1TenantsTenantIdWorklocations,
        PathValues.V1_TENANTS_TENANT_ID_JOBTITLES: V1TenantsTenantIdJobtitles,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_LEGAL_ENTITIES_LEGAL_ENTITY_ID_ATS_ATS_ACCOUNT_ID_JOBS: V1LegalEntitiesLegalEntityIdAtsAtsAccountIdJobs,
        PathValues.V1_LEGAL_ENTITIES_LEGAL_ENTITY_ID_ATS_ATS_ACCOUNT_ID_JOBS_ATS_JOB_ID: V1LegalEntitiesLegalEntityIdAtsAtsAccountIdJobsAtsJobId,
        PathValues.V1_LEGAL_ENTITIES_LEGAL_ENTITY_ID_ATS_ACCOUNTS: V1LegalEntitiesLegalEntityIdAtsAccounts,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_EMERGENCYCONTACT: V1EmployeesEmployeeIdEmergencycontact,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_CERTIFICATIONS: V1EmployeesEmployeeIdCertifications,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_CUSTOMFIELDS: V1EmployeesEmployeeIdCustomfields,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_DEDUCTIONS_EMPLOYEE_DEDUCTION_ID: V1EmployeesEmployeeIdDeductionsEmployeeDeductionId,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_DEDUCTIONS: V1EmployeesEmployeeIdDeductions,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_HSAACCOUNTS: V1EmployeesEmployeeIdHSAaccounts,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_DIRECT_DEPOSITS: V1EmployeesEmployeeIdDirectDeposits,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_DIRECT_DEPOSITS_DIRECT_DEPOSIT_ID: V1EmployeesEmployeeIdDirectDepositsDirectDepositId,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_PAYSTUB_DOCUMENT_DATA: V1EmployeesEmployeeIdPaystubDocumentData,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_PAY_STUB_DOCUMENT_DOCUMENT_ID: V1EmployeesEmployeeIdPayStubDocumentDocumentId,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_EARNINGS_EMPLOYEE_EARNING_ID: V1EmployeesEmployeeIdEarningsEmployeeEarningId,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_EARNINGS: V1EmployeesEmployeeIdEarnings,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_PAYROLLHOURS: V1LegalentitiesLegalEntityIdPayrollhours,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_PAYROLLHOURS: V1EmployeesEmployeeIdPayrollhours,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_I9VERIFICATION: V1EmployeesEmployeeIdI9Verification,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_PAYRATES: V1EmployeesEmployeeIdPayrates,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_PAYRATES_PAYRATE_ID: V1EmployeesEmployeeIdPayratesPayrateId,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_PAYSCHEDULE: V1EmployeesEmployeeIdPayschedule,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_PAYSTUBS: V1EmployeesEmployeeIdPaystubs,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_PAYSTUBS: V1LegalentitiesLegalEntityIdPaystubs,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_PAYSTUBSYTD: V1EmployeesEmployeeIdPaystubsytd,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_PAYSTUBSYTD: V1LegalentitiesLegalEntityIdPaystubsytd,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_SCHEDULES: V1EmployeesEmployeeIdSchedules,
        PathValues.V1_LEGAL_ENTITIES_LEGAL_ENTITY_ID_SCHEDULES: V1LegalEntitiesLegalEntityIdSchedules,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_SCHEDULES_SCHEDULE_ID: V1EmployeesEmployeeIdSchedulesScheduleId,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID: V1EmployeesEmployeeId,
        PathValues.V1_TENANTS_TENANT_ID_EMPLOYEES: V1TenantsTenantIdEmployees,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_EMPLOYEES: V1LegalentitiesLegalEntityIdEmployees,
        PathValues.V1_EMPLOYEES: V1Employees,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_POSITIONANDSTATUS: V1EmployeesEmployeeIdPositionandstatus,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_POSITION: V1EmployeesEmployeeIdPosition,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_STATUS: V1EmployeesEmployeeIdStatus,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_IDENTIFYINGDATA: V1EmployeesEmployeeIdIdentifyingdata,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_EMPLOYEES_IDENTIFYING_DATA: V1LegalentitiesLegalEntityIdEmployeesIdentifyingData,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_PAYGROUP: V1EmployeesEmployeeIdPaygroup,
        PathValues.V1_EMPLOYEES_ONBOARDING: V1EmployeesOnboarding,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_ONBOARDINGEMPLOYEES: V1LegalentitiesLegalEntityIdOnboardingemployees,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_TAXES: V1EmployeesEmployeeIdTaxes,
        PathValues.V1_EMPLOYEES_TAXES_FILING_STATUS_TAX_CODE: V1EmployeesTaxesFilingStatusTaxCode,
        PathValues.V1_EMPLOYEES_TAXES_TAX_FIELDS_TAX_CODE: V1EmployeesTaxesTaxFieldsTaxCode,
        PathValues.V1_LEGAL_ENTITIES_LEGAL_ENTITY_ID_PUNCHES: V1LegalEntitiesLegalEntityIdPunches,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_PUNCHES: V1EmployeesEmployeeIdPunches,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_TIMEOFFACCRUALS: V1EmployeesEmployeeIdTimeoffaccruals,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_TIMEOFFACCRUALS: V1LegalentitiesLegalEntityIdTimeoffaccruals,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_TIMEOFFREQUESTS: V1EmployeesEmployeeIdTimeoffrequests,
        PathValues.V1_EVENTS_MOCKEVENT: V1EventsMockevent,
        PathValues.V1_GENERALLEDGER_LEGALENTITIES_LEGAL_ENTITY_ID: V1GeneralledgerLegalentitiesLegalEntityId,
        PathValues.V1_GENERALLEDGER_JOBCOSTING_LEGALENTITIES_LEGAL_ENTITY_ID: V1GeneralledgerJobcostingLegalentitiesLegalEntityId,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_LABORCATEGORIES: V1LegalentitiesLegalEntityIdLaborcategories,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_LABORCODES: V1LegalentitiesLegalEntityIdLaborcodes,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID: V1LegalentitiesLegalEntityId,
        PathValues.V1_LEGALENTITIES_ACTIVATED_LEGAL_ENTITY_TENANT_LIST: V1LegalentitiesActivatedLegalEntityTenantList,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_CERTIFICATION_ORGANIZATIONS: V1LegalentitiesLegalEntityIdCertificationOrganizations,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_CERTIFICATIONS: V1LegalentitiesLegalEntityIdCertifications,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_DEDUCTIONS: V1LegalentitiesLegalEntityIdDeductions,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_DEPARTMENTS: V1LegalentitiesLegalEntityIdDepartments,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_DEPARTMENTS_DEPARTMENT_ID: V1LegalentitiesLegalEntityIdDepartmentsDepartmentId,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_EARNINGS: V1LegalentitiesLegalEntityIdEarnings,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_JOBTITLES: V1LegalentitiesLegalEntityIdJobtitles,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_PAYDATA: V1LegalentitiesLegalEntityIdPaydata,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_PAY_GROUPS: V1LegalentitiesLegalEntityIdPayGroups,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_PAYROLL_PROCESSING: V1LegalentitiesLegalEntityIdPayrollProcessing,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_PAYSCHEDULE: V1LegalentitiesLegalEntityIdPayschedule,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_ACTIVITYTYPES: V1LegalentitiesLegalEntityIdActivitytypes,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_SCHEDULEGROUPS: V1LegalentitiesLegalEntityIdSchedulegroups,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_SERVICES: V1LegalentitiesLegalEntityIdServices,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_STATUS_REASONS_STATUS_CATEGORY: V1LegalentitiesLegalEntityIdStatusReasonsStatusCategory,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_TAXES: V1LegalentitiesLegalEntityIdTaxes,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_TIMEOFFREQUESTS: V1LegalentitiesLegalEntityIdTimeoffrequests,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_TIMEOFF_REQUESTS_TIMEOFF_REQUEST_ID: V1LegalentitiesLegalEntityIdTimeoffRequestsTimeoffRequestId,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_TIMEOFF_REQUESTSERRORLOG_TRACKING_ID: V1LegalentitiesLegalEntityIdTimeoffRequestserrorlogTrackingId,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_TIMEOFFTYPES: V1LegalentitiesLegalEntityIdTimeofftypes,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_WORKLOCATIONS: V1LegalentitiesLegalEntityIdWorklocations,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_WORKLOCATIONS_WORK_LOCATION_ID: V1LegalentitiesLegalEntityIdWorklocationsWorkLocationId,
        PathValues.V1_LEGALENTITIES_LEGAL_ENTITY_ID_WORKSITES: V1LegalentitiesLegalEntityIdWorksites,
        PathValues.V1_LEGAL_ENTITIES_LEGAL_ENTITY_ID_PERSONS: V1LegalEntitiesLegalEntityIdPersons,
        PathValues.V1_TENANTS_TENANT_ID_PERSONS: V1TenantsTenantIdPersons,
        PathValues.V1_TENANTS_TENANT_ID_PERSONS_PERSON_ID: V1TenantsTenantIdPersonsPersonId,
        PathValues.V1_EMPLOYEES_EMPLOYEE_ID_PERSON: V1EmployeesEmployeeIdPerson,
        PathValues.V1_TENANTS_TENANT_ID: V1TenantsTenantId,
        PathValues.V1_TENANTS_TENANT_ID_WORKLOCATIONS: V1TenantsTenantIdWorklocations,
        PathValues.V1_TENANTS_TENANT_ID_JOBTITLES: V1TenantsTenantIdJobtitles,
    }
)
