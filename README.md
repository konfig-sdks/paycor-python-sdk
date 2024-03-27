<div align="left">

[![Visit Paycor](./header.png)](https://paycor.com)

# Paycor<a id="paycor"></a>


Welcome to Paycor's Public API! This document is a reference for the APIs Paycor has available, and acts as a complement to the \"Guides\" section. 

# Getting Started<a id="getting-started"></a>

<strong>To learn more about getting started with Paycor's Public APIs, check out our <a href=\"/guides\">Guides.</a></strong>

# GET, PUT, POST<a id="get-put-post"></a>

* When requesting object, use GET endpoints. All list endpoints support paging, as described [in the other doc]. 
* When creating an object, use POST endpoints. Your code will need to create an object and send it to Paycor in your API call request body as JSON. You can use the \"request sample\" body as a starting point. Our endpoints will return a reference to the created object (the ID and GET API URL) for your system.
* When updating an object, you will use PUT endpoints. The general flow would be to: GET the object you want to update, modify the fields as desired, then PUT the object (as JSON in the request body) to our endpoints. Some fields like the object's ID cannot be updated because they are system-set.'


# Error Handling<a id="error-handling"></a>

* 400: Please consult the response text to correct your request information. 
* 401 with response \"Access denied due to missing subscription key\": Please include your APIM Subscription Key as header Ocp-Apim-Subscription-Key or querystring parameter subscription-key. 
* 401 with no response: Please ensure you included a valid & current Access Token in the Authorization header.
* 403: Please ensure your Access Token's scope has all the relevant access you need, on the AppCreator Data Access screen. 
* 404: Please validate the API route you are using. If that is correct, one of your IDs most likely does not exist or is not in a valid state. 
* 429: Paycor implements rate limits for our Public API. Each customer (implemented via APIM subscription key) has a limited number of calls. The number of calls is counted across all APIs, not per individual API. Please use bulk endpoints where available and spread your calls over a wider timespan.
  * The default rate limit is up to 1000 API calls per minute (total across all our Public APIs). 
* 500: Please contact Paycor. When you make a POST or PUT call and receive a 500, please do not retry the call automatically - this may result in double-posting. GETs can be safely retried.


# IDs<a id="ids"></a>

* ClientId = LegalEntityId
* TenantId = CompanyId
* EmployeeId is not visible in Paycor's UI, you must retrieve it from the Public API

# Earnings, Deductions, Taxes<a id="earnings-deductions-taxes"></a>

This section describes the domain model for Paycor's Earnings, Deductions, and Taxes. This will provide background for many paydata-related Public API endpoints. 

Paycor stores Earnings, Deductions, and Taxes each at three levels:
* Global: Same data across all legal entities. Setup by Paycor for customers to choose from. Sample Codes (note these will not be setup on every Legal Entity):
  * Earnings: REG, OT
  * Taxes: FITWH, SOC, SOCER, OHCIN
  * Deductions: 401k, KMat, H125, UWay
* Legal Entity or Tenant: Codes setup &amp; customized on the legal entity or Tenant level. Must be tied to a Global Code. 
  * Perform UI allows creating Deduction and Earning codes on Tenant level (under Configure Company nav menu). These will be returned by the Legal Entity Public API endpoints. 
* Employee: codes setup on a particular employee, tied to a Legal Entity-level or Tenant-level code
  * Employee Earnings/Deductions/Taxes are applied during payroll. Many properties are inherited from the Legal Entity or Global levels, but some can be overridden. 

# Authentication<a id="authentication"></a>

<!-- ReDoc-Inject: <security-definitions> -->


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`paycor._legal_entity_taxes.get_by_legal_entity_id`](#paycor_legal_entity_taxesget_by_legal_entity_id)
  * [`paycor.applicant_tracking_system.get_account_jobs`](#paycorapplicant_tracking_systemget_account_jobs)
  * [`paycor.applicant_tracking_system.get_job_by_job_id`](#paycorapplicant_tracking_systemget_job_by_job_id)
  * [`paycor.applicant_tracking_system.list_ats_accounts_by_legal_entity`](#paycorapplicant_tracking_systemlist_ats_accounts_by_legal_entity)
  * [`paycor.employee_(legacy_/_perform_time)_schedules.add_to_employee`](#paycoremployee_legacy__perform_time_schedulesadd_to_employee)
  * [`paycor.employee_(legacy_/_perform_time)_schedules.delete_legacy_schedule`](#paycoremployee_legacy__perform_time_schedulesdelete_legacy_schedule)
  * [`paycor.employee_(legacy_/_perform_time)_schedules.get_by_employee_id`](#paycoremployee_legacy__perform_time_schedulesget_by_employee_id)
  * [`paycor.employee_(legacy_/_perform_time)_schedules.get_by_legal_entity_id`](#paycoremployee_legacy__perform_time_schedulesget_by_legal_entity_id)
  * [`paycor.employee_certifications.add_new_certification`](#paycoremployee_certificationsadd_new_certification)
  * [`paycor.employee_certifications.list_by_employee_id`](#paycoremployee_certificationslist_by_employee_id)
  * [`paycor.employee_certifications.update_certification`](#paycoremployee_certificationsupdate_certification)
  * [`paycor.employee_custom_fields.get_by_employee_id`](#paycoremployee_custom_fieldsget_by_employee_id)
  * [`paycor.employee_custom_fields.update_by_employee_id`](#paycoremployee_custom_fieldsupdate_by_employee_id)
  * [`paycor.employee_deductions.add_deduction_to_employee`](#paycoremployee_deductionsadd_deduction_to_employee)
  * [`paycor.employee_deductions.get_by_employee_id`](#paycoremployee_deductionsget_by_employee_id)
  * [`paycor.employee_deductions.get_by_employee_id_and_deduction_id`](#paycoremployee_deductionsget_by_employee_id_and_deduction_id)
  * [`paycor.employee_deductions.update_by_employee_id`](#paycoremployee_deductionsupdate_by_employee_id)
  * [`paycor.employee_direct_deposits.add_by_employee_id`](#paycoremployee_direct_depositsadd_by_employee_id)
  * [`paycor.employee_direct_deposits.add_by_employee_id_hsa`](#paycoremployee_direct_depositsadd_by_employee_id_hsa)
  * [`paycor.employee_direct_deposits.get_by_employee_and_deposit_id`](#paycoremployee_direct_depositsget_by_employee_and_deposit_id)
  * [`paycor.employee_direct_deposits.get_by_employee_id`](#paycoremployee_direct_depositsget_by_employee_id)
  * [`paycor.employee_direct_deposits.get_by_employee_id_hsa`](#paycoremployee_direct_depositsget_by_employee_id_hsa)
  * [`paycor.employee_direct_deposits.update_by_employee_id_ddd`](#paycoremployee_direct_depositsupdate_by_employee_id_ddd)
  * [`paycor.employee_direct_deposits.update_hsa_direct_deposits_by_employee_id`](#paycoremployee_direct_depositsupdate_hsa_direct_deposits_by_employee_id)
  * [`paycor.employee_documents.download_pay_stub`](#paycoremployee_documentsdownload_pay_stub)
  * [`paycor.employee_documents.get_pay_stub_document_by_employee_id`](#paycoremployee_documentsget_pay_stub_document_by_employee_id)
  * [`paycor.employee_earnings.add_new_earning`](#paycoremployee_earningsadd_new_earning)
  * [`paycor.employee_earnings.get_by_employee_and_earning`](#paycoremployee_earningsget_by_employee_and_earning)
  * [`paycor.employee_earnings.get_by_employee_id`](#paycoremployee_earningsget_by_employee_id)
  * [`paycor.employee_earnings.update_data`](#paycoremployee_earningsupdate_data)
  * [`paycor.employee_emergency_contact.create_update`](#paycoremployee_emergency_contactcreate_update)
  * [`paycor.employee_i9_verification.get_by_employee_id`](#paycoremployee_i9_verificationget_by_employee_id)
  * [`paycor.employee_i9_verification.update_by_employee_id_i9_verification`](#paycoremployee_i9_verificationupdate_by_employee_id_i9_verification)
  * [`paycor.employee_onboarding.add_new_entry`](#paycoremployee_onboardingadd_new_entry)
  * [`paycor.employee_onboarding.list_onboarding_employees`](#paycoremployee_onboardinglist_onboarding_employees)
  * [`paycor.employee_pay_rates.add_new_rate`](#paycoremployee_pay_ratesadd_new_rate)
  * [`paycor.employee_pay_rates.get_by_employee_id`](#paycoremployee_pay_ratesget_by_employee_id)
  * [`paycor.employee_pay_rates.update_by_employee_id_and_payrate_id`](#paycoremployee_pay_ratesupdate_by_employee_id_and_payrate_id)
  * [`paycor.employee_pay_schedule.get_upcoming_check_dates`](#paycoremployee_pay_scheduleget_upcoming_check_dates)
  * [`paycor.employee_pay_stubs.get_by_employee_id`](#paycoremployee_pay_stubsget_by_employee_id)
  * [`paycor.employee_pay_stubs.get_by_legal_entity`](#paycoremployee_pay_stubsget_by_legal_entity)
  * [`paycor.employee_pay_stubs.get_ytd_by_employee_id`](#paycoremployee_pay_stubsget_ytd_by_employee_id)
  * [`paycor.employee_pay_stubs.get_ytd_by_legal_entity`](#paycoremployee_pay_stubsget_ytd_by_legal_entity)
  * [`paycor.employee_payroll_hours.add_hours_and_earnings_to_paygrid`](#paycoremployee_payroll_hoursadd_hours_and_earnings_to_paygrid)
  * [`paycor.employee_payroll_hours.import_to_employee`](#paycoremployee_payroll_hoursimport_to_employee)
  * [`paycor.employee_taxes.add_by_employee_id`](#paycoremployee_taxesadd_by_employee_id)
  * [`paycor.employee_taxes.get_by_employee_id`](#paycoremployee_taxesget_by_employee_id)
  * [`paycor.employee_taxes.get_filing_status_by_tax_code`](#paycoremployee_taxesget_filing_status_by_tax_code)
  * [`paycor.employee_taxes.get_tax_fields_by_tax_code`](#paycoremployee_taxesget_tax_fields_by_tax_code)
  * [`paycor.employee_taxes.update_by_employee_id`](#paycoremployee_taxesupdate_by_employee_id)
  * [`paycor.employee_time_card_punches.get_by_employee_id`](#paycoremployee_time_card_punchesget_by_employee_id)
  * [`paycor.employee_time_card_punches.get_by_legal_entity_id`](#paycoremployee_time_card_punchesget_by_legal_entity_id)
  * [`paycor.employee_time_off_accruals.get_by_employee_id`](#paycoremployee_time_off_accrualsget_by_employee_id)
  * [`paycor.employee_time_off_accruals.get_by_legal_entity_id`](#paycoremployee_time_off_accrualsget_by_legal_entity_id)
  * [`paycor.employees.create_new_employee`](#paycoremployeescreate_new_employee)
  * [`paycor.employees.get_by_employee_id`](#paycoremployeesget_by_employee_id)
  * [`paycor.employees.get_identifying_data`](#paycoremployeesget_identifying_data)
  * [`paycor.employees.list_by_legal_entity_id`](#paycoremployeeslist_by_legal_entity_id)
  * [`paycor.employees.list_by_tenant_id`](#paycoremployeeslist_by_tenant_id)
  * [`paycor.employees.update_contact`](#paycoremployeesupdate_contact)
  * [`paycor.employees.update_paygroup`](#paycoremployeesupdate_paygroup)
  * [`paycor.employees.update_personal_data`](#paycoremployeesupdate_personal_data)
  * [`paycor.employees.update_position_and_status_data`](#paycoremployeesupdate_position_and_status_data)
  * [`paycor.employees.update_position_data`](#paycoremployeesupdate_position_data)
  * [`paycor.employees.update_status_data`](#paycoremployeesupdate_status_data)
  * [`paycor.events.notify_event_details`](#paycoreventsnotify_event_details)
  * [`paycor.general_ledger.get_by_legal_entity_id`](#paycorgeneral_ledgerget_by_legal_entity_id)
  * [`paycor.general_ledger_job_costing.get_by_legal_entity_id`](#paycorgeneral_ledger_job_costingget_by_legal_entity_id)
  * [`paycor.job_titles.list_by_tenant_id`](#paycorjob_titleslist_by_tenant_id)
  * [`paycor.labor_categories.by_legal_entity_id_get`](#paycorlabor_categoriesby_legal_entity_id_get)
  * [`paycor.labor_codes.add_labor_code_to_legal_entity`](#paycorlabor_codesadd_labor_code_to_legal_entity)
  * [`paycor.labor_codes.list_by_legal_entity_id`](#paycorlabor_codeslist_by_legal_entity_id)
  * [`paycor.labor_codes.update_specified_labor_code`](#paycorlabor_codesupdate_specified_labor_code)
  * [`paycor.legal_entities.get_by_id`](#paycorlegal_entitiesget_by_id)
  * [`paycor.legal_entities.get_tenant_list`](#paycorlegal_entitiesget_tenant_list)
  * [`paycor.legal_entity_activity_types.get_by_legal_entity_id`](#paycorlegal_entity_activity_typesget_by_legal_entity_id)
  * [`paycor.legal_entity_certifications.list`](#paycorlegal_entity_certificationslist)
  * [`paycor.legal_entity_certifications.list_certification_organizations`](#paycorlegal_entity_certificationslist_certification_organizations)
  * [`paycor.legal_entity_deductions.view_employees_data`](#paycorlegal_entity_deductionsview_employees_data)
  * [`paycor.legal_entity_departments.create_new_department`](#paycorlegal_entity_departmentscreate_new_department)
  * [`paycor.legal_entity_departments.get_by_id`](#paycorlegal_entity_departmentsget_by_id)
  * [`paycor.legal_entity_departments.list_by_legal_entity_id`](#paycorlegal_entity_departmentslist_by_legal_entity_id)
  * [`paycor.legal_entity_departments.update_by_legal_entity_id`](#paycorlegal_entity_departmentsupdate_by_legal_entity_id)
  * [`paycor.legal_entity_earnings.get_by_legal_entity_id`](#paycorlegal_entity_earningsget_by_legal_entity_id)
  * [`paycor.legal_entity_job_titles.list_by_legal_entity_id`](#paycorlegal_entity_job_titleslist_by_legal_entity_id)
  * [`paycor.legal_entity_pay_data.get_pay_dates`](#paycorlegal_entity_pay_dataget_pay_dates)
  * [`paycor.legal_entity_pay_groups.list_by_legal_entity_id`](#paycorlegal_entity_pay_groupslist_by_legal_entity_id)
  * [`paycor.legal_entity_pay_schedule.get_by_legal_entity_and_paygroup`](#paycorlegal_entity_pay_scheduleget_by_legal_entity_and_paygroup)
  * [`paycor.legal_entity_payroll_processing_data.get_by_legal_entity`](#paycorlegal_entity_payroll_processing_dataget_by_legal_entity)
  * [`paycor.legal_entity_schedule_groups.get_by_legal_entity_id`](#paycorlegal_entity_schedule_groupsget_by_legal_entity_id)
  * [`paycor.legal_entity_services.get_subscribed_services`](#paycorlegal_entity_servicesget_subscribed_services)
  * [`paycor.legal_entity_status_reason.get_list`](#paycorlegal_entity_status_reasonget_list)
  * [`paycor.legal_entity_time_data.get_time_off_request_error_logs_by_tracking_id`](#paycorlegal_entity_time_dataget_time_off_request_error_logs_by_tracking_id)
  * [`paycor.legal_entity_time_off_types.view_time_off_types`](#paycorlegal_entity_time_off_typesview_time_off_types)
  * [`paycor.legal_entity_work_locations.add_by_legal_entity_id`](#paycorlegal_entity_work_locationsadd_by_legal_entity_id)
  * [`paycor.legal_entity_work_locations.delete_by_legal_entity_and_work_location_id`](#paycorlegal_entity_work_locationsdelete_by_legal_entity_and_work_location_id)
  * [`paycor.legal_entity_work_locations.get_by_legal_entity_and_location`](#paycorlegal_entity_work_locationsget_by_legal_entity_and_location)
  * [`paycor.legal_entity_work_locations.list`](#paycorlegal_entity_work_locationslist)
  * [`paycor.legal_entity_work_locations.update_by_legal_entity_id`](#paycorlegal_entity_work_locationsupdate_by_legal_entity_id)
  * [`paycor.legal_entity_work_sites.get_by_legal_entity_id`](#paycorlegal_entity_work_sitesget_by_legal_entity_id)
  * [`paycor.persons.get_by_employee_id_person`](#paycorpersonsget_by_employee_id_person)
  * [`paycor.persons.get_by_tenant_and_person`](#paycorpersonsget_by_tenant_and_person)
  * [`paycor.persons.list_by_legal_entity_id`](#paycorpersonslist_by_legal_entity_id)
  * [`paycor.persons.list_by_tenant_id`](#paycorpersonslist_by_tenant_id)
  * [`paycor.tenants.get_by_id`](#paycortenantsget_by_id)
  * [`paycor.tenants.get_work_locations_by_tenant_id`](#paycortenantsget_work_locations_by_tenant_id)
  * [`paycor.time_off_requests.get_timeoff_request_by_id`](#paycortime_off_requestsget_timeoff_request_by_id)
  * [`paycor.time_off_requests.list_by_employee_id`](#paycortime_off_requestslist_by_employee_id)
  * [`paycor.time_off_requests.list_by_legal_entity_id`](#paycortime_off_requestslist_by_legal_entity_id)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Paycor&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from paycor_python_sdk import Paycor, ApiException

paycor = Paycor(

        access_token = 'YOUR_API_KEY',

        apim_subscription_key = 'YOUR_API_KEY',
)

try:
    # Get Legal Entity Taxes by Legal Entity ID
    get_by_legal_entity_id_response = paycor._legal_entity_taxes.get_by_legal_entity_id(
        legal_entity_id=1,
        continuation_token="string_example",
    )
    print(get_by_legal_entity_id_response)
except ApiException as e:
    print("Exception when calling LegalEntityTaxesApi.get_by_legal_entity_id: %s\n" % e)
    pprint(e.body)
    if e.status == 500:
        pprint(e.body["correlation_id"])
        pprint(e.body["title"])
        pprint(e.body["detail"])
        pprint(e.body["source"])
    if e.status == 404:
        pprint(e.body["correlation_id"])
        pprint(e.body["title"])
        pprint(e.body["detail"])
        pprint(e.body["source"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from paycor_python_sdk import Paycor, ApiException

paycor = Paycor(

        access_token = 'YOUR_API_KEY',

        apim_subscription_key = 'YOUR_API_KEY',
)

async def main():
    try:
        # Get Legal Entity Taxes by Legal Entity ID
        get_by_legal_entity_id_response = await paycor._legal_entity_taxes.aget_by_legal_entity_id(
            legal_entity_id=1,
            continuation_token="string_example",
        )
        print(get_by_legal_entity_id_response)
    except ApiException as e:
        print("Exception when calling LegalEntityTaxesApi.get_by_legal_entity_id: %s\n" % e)
        pprint(e.body)
        if e.status == 500:
            pprint(e.body["correlation_id"])
            pprint(e.body["title"])
            pprint(e.body["detail"])
            pprint(e.body["source"])
        if e.status == 404:
            pprint(e.body["correlation_id"])
            pprint(e.body["title"])
            pprint(e.body["detail"])
            pprint(e.body["source"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from paycor_python_sdk import Paycor, ApiException

paycor = Paycor(

        access_token = 'YOUR_API_KEY',

        apim_subscription_key = 'YOUR_API_KEY',
)

try:
    # Get Legal Entity Taxes by Legal Entity ID
    get_by_legal_entity_id_response = paycor._legal_entity_taxes.raw.get_by_legal_entity_id(
        legal_entity_id=1,
        continuation_token="string_example",
    )
    pprint(get_by_legal_entity_id_response.body)
    pprint(get_by_legal_entity_id_response.headers)
    pprint(get_by_legal_entity_id_response.status)
    pprint(get_by_legal_entity_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling LegalEntityTaxesApi.get_by_legal_entity_id: %s\n" % e)
    pprint(e.body)
    if e.status == 500:
        pprint(e.body["correlation_id"])
        pprint(e.body["title"])
        pprint(e.body["detail"])
        pprint(e.body["source"])
    if e.status == 404:
        pprint(e.body["correlation_id"])
        pprint(e.body["title"])
        pprint(e.body["detail"])
        pprint(e.body["source"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `paycor._legal_entity_taxes.get_by_legal_entity_id`<a id="paycor_legal_entity_taxesget_by_legal_entity_id"></a>

Data access: View Legal Entity Taxes

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_legal_entity_id_response = paycor._legal_entity_taxes.get_by_legal_entity_id(
    legal_entity_id=1,
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of the Legal Entity you want to get (synonymous to Paycor's ClientID) the taxes

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get the next set of Legal Entity taxes

#### 🔄 Return<a id="🔄-return"></a>

[`LegalEntityTaxesGetByLegalEntityIdResponse`](./paycor_python_sdk/pydantic/legal_entity_taxes_get_by_legal_entity_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/taxes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.applicant_tracking_system.get_account_jobs`<a id="paycorapplicant_tracking_systemget_account_jobs"></a>

Data Access: View ATS Account jobs by ATS Account ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_account_jobs_response = paycor.applicant_tracking_system.get_account_jobs(
    legal_entity_id=1,
    ats_account_id="atsAccountId_example",
    include=[
        "string_example"
    ],
    posted_to_careers=True,
    status="ACTIVE",
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

Paycor Legal Entity ID of the legal entity for which you want to get the ATS account jobs

##### ats_account_id: `Optional[str]`<a id="ats_account_id-optionalstr"></a>

ATS account ID of for which you want to get the ATS account jobs

##### include: List[[`Includes`](./paycor_python_sdk/type/includes.py)]<a id="include-listincludespaycor_python_sdktypeincludespy"></a>

Options to include more data: All, Hiring managers, Recruiters, Team members, Executives

##### posted_to_careers: `Optional[bool]`<a id="posted_to_careers-optionalbool"></a>

Option to filter jobs based on if they are posted to the careers page

##### status: [`JobStatus`](./paycor_python_sdk/type/.py)<a id="status-jobstatuspaycor_python_sdktypepy"></a>

Option to filter jobs by status

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfJob`](./paycor_python_sdk/pydantic/paged_result_of_job.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalEntities/{legalEntityId}/ats/{atsAccountId}/jobs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.applicant_tracking_system.get_job_by_job_id`<a id="paycorapplicant_tracking_systemget_job_by_job_id"></a>

Data Access: View ATS Account Job by ATS Job Id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_job_by_job_id_response = paycor.applicant_tracking_system.get_job_by_job_id(
    legal_entity_id=1,
    ats_account_id="atsAccountId_example",
    ats_job_id="atsJobId_example",
    include=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

Paycor Legal Entity ID of the legal entity for which you want to get the ATS account job

##### ats_account_id: `Optional[str]`<a id="ats_account_id-optionalstr"></a>

ATS account ID of for which you want to get the ATS account job

##### ats_job_id: `Optional[str]`<a id="ats_job_id-optionalstr"></a>

ATS Job ID

##### include: List[[`Includes2`](./paycor_python_sdk/type/includes2.py)]<a id="include-listincludes2paycor_python_sdktypeincludes2py"></a>

Options to include more data: All, Hiring managers, Recruiters, Team members, Executives

#### 🔄 Return<a id="🔄-return"></a>

[`Job`](./paycor_python_sdk/pydantic/job.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalEntities/{legalEntityId}/ats/{atsAccountId}/jobs/{atsJobId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.applicant_tracking_system.list_ats_accounts_by_legal_entity`<a id="paycorapplicant_tracking_systemlist_ats_accounts_by_legal_entity"></a>

Data Access: View ATS Accounts By Legal Entity Id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_ats_accounts_by_legal_entity_response = paycor.applicant_tracking_system.list_ats_accounts_by_legal_entity(
    legal_entity_id=1,
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

Paycor Legal Entity ID of the legal entity for which you want to get the ATS accounts

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ATSAccount`](./paycor_python_sdk/pydantic/ats_account.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalEntities/{legalEntityId}/ats/accounts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_(legacy_/_perform_time)_schedules.add_to_employee`<a id="paycoremployee_legacy__perform_time_schedulesadd_to_employee"></a>

Data Access: Create Legacy/Perform Time Employee Schedule

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_to_employee_response = paycor.employee_(legacy_/_perform_time)_schedules.add_to_employee(
    employee_id="employeeId_example",
    start_date_time="2019-11-01T00:00:00Z",
    end_date_time="2019-11-01T00:00:00Z",
    before_start_time_in_minutes=120,
    after_end_time_in_minutes=120,
    label="MorningShift",
    shift_depeartment_id="2f28bd9c-a39e-41f1-b40f-b44bf2e9c265",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

ID of an Employee for whom you want to add a schedule

##### start_date_time: `datetime`<a id="start_date_time-datetime"></a>

Date and time the employee will begin work. Format: YYYY-MM-DDTHH:MM:SSZ  (ISO-8601 standard)             

##### end_date_time: `datetime`<a id="end_date_time-datetime"></a>

Date and time the employee will stop work. Format: YYYY-MM-DDTHH:MM:SSZ  (ISO-8601 standard)             

##### before_start_time_in_minutes: `Optional[int]`<a id="before_start_time_in_minutes-optionalint"></a>

Punches will be tied to the schedule if employee clocks in this many Minutes before shift starts.

##### after_end_time_in_minutes: `Optional[int]`<a id="after_end_time_in_minutes-optionalint"></a>

Punches will be tied to the schedule if employee clocks out this many Minutes after shift ends.

##### label: `Optional[str]`<a id="label-optionalstr"></a>

This is the label that will be assigned to the shift.             

##### shift_depeartment_id: `Optional[str]`<a id="shift_depeartment_id-optionalstr"></a>

Unique identifier of the Department where the employee's timecard will be created.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Schedule2`](./paycor_python_sdk/type/schedule2.py)
Employee Schedule object to insert

#### 🔄 Return<a id="🔄-return"></a>

[`CreateOrUpdateResponse`](./paycor_python_sdk/pydantic/create_or_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/schedules` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_(legacy_/_perform_time)_schedules.delete_legacy_schedule`<a id="paycoremployee_legacy__perform_time_schedulesdelete_legacy_schedule"></a>

Data Access: Delete Legacy/Perform Time Employee Schedule

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paycor.employee_(legacy_/_perform_time)_schedules.delete_legacy_schedule(
    employee_id="employeeId_example",
    schedule_id="scheduleId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

Employee ID of the schedule record you want to delete

##### schedule_id: `str`<a id="schedule_id-str"></a>

Schedule ID to delete

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/schedules/{scheduleId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_(legacy_/_perform_time)_schedules.get_by_employee_id`<a id="paycoremployee_legacy__perform_time_schedulesget_by_employee_id"></a>

Date requirements:
* Start Date and End Date must not be more than one year ago
* Start Date must not be in future
* Start date and end date range can be no greater than 90 days

Data Access: View Legacy/Perform Employee Schedules by Employee Id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_employee_id_response = paycor.employee_(legacy_/_perform_time)_schedules.get_by_employee_id(
    employee_id="employeeId_example",
    start_date="1970-01-01T00:00:00.00Z",
    end_date="1970-01-01T00:00:00.00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

ID of employee for which you want to get schedules

##### start_date: `datetime`<a id="start_date-datetime"></a>

Date range filter, showing which records to return

##### end_date: `datetime`<a id="end_date-datetime"></a>

Date range filter, showing which records to return

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeLegacyPerformTimeSchedulesGetByEmployeeIdResponse`](./paycor_python_sdk/pydantic/employee_legacy_perform_time_schedules_get_by_employee_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/schedules` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_(legacy_/_perform_time)_schedules.get_by_legal_entity_id`<a id="paycoremployee_legacy__perform_time_schedulesget_by_legal_entity_id"></a>

Date requirements:
* Start Date and End Date must not be more than one year ago
* Start Date must not be in future
* Start date and end date range can be no greater than 90 days

Data Access: View Legacy/Perform Employee Schedules by Legal Entity Id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_legal_entity_id_response = paycor.employee_(legacy_/_perform_time)_schedules.get_by_legal_entity_id(
    legal_entity_id=1,
    start_date="1970-01-01T00:00:00.00Z",
    end_date="1970-01-01T00:00:00.00Z",
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of Legal Entity for which you want to get schedules

##### start_date: `datetime`<a id="start_date-datetime"></a>

Date range filter, showing which records to return

##### end_date: `datetime`<a id="end_date-datetime"></a>

Date range filter, showing which records to return

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfEmployeeSchedule`](./paycor_python_sdk/pydantic/paged_result_of_employee_schedule.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalEntities/{legalEntityId}/schedules` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_certifications.add_new_certification`<a id="paycoremployee_certificationsadd_new_certification"></a>

Data Access: Create and Update Certification

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_new_certification_response = paycor.employee_certifications.add_new_certification(
    certification_name="First Aid certificate",
    employee_id="employeeId_example",
    effective_date="2022-03-09",
    expiration_date="2022-03-19",
    certification_number="436576",
    certification_organization_name="Red Cross",
    notes="note: expires soon",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### certification_name: `str`<a id="certification_name-str"></a>

Name of certification             

##### employee_id: `str`<a id="employee_id-str"></a>

ID of an Employee for whom you want to add the certification

##### effective_date: `Optional[datetime]`<a id="effective_date-optionaldatetime"></a>

Effective date of certification             

##### expiration_date: `Optional[datetime]`<a id="expiration_date-optionaldatetime"></a>

Expiration date of certification             

##### certification_number: `Optional[str]`<a id="certification_number-optionalstr"></a>

Number of certification             

##### certification_organization_name: `Optional[str]`<a id="certification_organization_name-optionalstr"></a>

Name of certification organization             

##### notes: `Optional[str]`<a id="notes-optionalstr"></a>

Note on certification             

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Certification`](./paycor_python_sdk/type/certification.py)
Certification object

#### 🔄 Return<a id="🔄-return"></a>

[`CreateOrUpdateResponse`](./paycor_python_sdk/pydantic/create_or_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/certifications` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_certifications.list_by_employee_id`<a id="paycoremployee_certificationslist_by_employee_id"></a>

Data Access: View Certification Information for Employee

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_by_employee_id_response = paycor.employee_certifications.list_by_employee_id(
    employee_id="employeeId_example",
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

ID of the employee for which you want to get the certifications

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfEmployeeCertification`](./paycor_python_sdk/pydantic/paged_result_of_employee_certification.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/certifications` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_certifications.update_certification`<a id="paycoremployee_certificationsupdate_certification"></a>

Data Access: Create and Update Certification

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_certification_response = paycor.employee_certifications.update_certification(
    employee_certification_id="FDB487C7-E853-4097-8697-B705AC3C7ABF",
    employee_id="employeeId_example",
    certification_number="436576",
    effective_date="2022-03-09",
    expiration_date="2022-03-19",
    notes="note: expires soon",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_certification_id: `str`<a id="employee_certification_id-str"></a>

Id of employee certification             

##### employee_id: `str`<a id="employee_id-str"></a>

ID of the employee for which you want to update the certifications

##### certification_number: `Optional[str]`<a id="certification_number-optionalstr"></a>

Number of certification             

##### effective_date: `Optional[datetime]`<a id="effective_date-optionaldatetime"></a>

Effective date of certification             

##### expiration_date: `Optional[datetime]`<a id="expiration_date-optionaldatetime"></a>

Expiration date of certification             

##### notes: `Optional[str]`<a id="notes-optionalstr"></a>

Note on certification             

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeCertification2`](./paycor_python_sdk/type/employee_certification2.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CreateOrUpdateResponse`](./paycor_python_sdk/pydantic/create_or_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/certifications` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_custom_fields.get_by_employee_id`<a id="paycoremployee_custom_fieldsget_by_employee_id"></a>

Data Access: View Employee Custom Fields

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_employee_id_response = paycor.employee_custom_fields.get_by_employee_id(
    employee_id="employeeId_example",
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

ID of the employee for whom you want to get the custom fields

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get the next set of employee custom fields

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeCustomFieldsGetByEmployeeIdResponse`](./paycor_python_sdk/pydantic/employee_custom_fields_get_by_employee_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/customfields` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_custom_fields.update_by_employee_id`<a id="paycoremployee_custom_fieldsupdate_by_employee_id"></a>

Data Access: Update Employee Custom Fields

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_employee_id_response = paycor.employee_custom_fields.update_by_employee_id(
    body=[
        {
            "custom_field_id": "7b64160b-0a3a-0000-0000-000014e00100",
            "value": "Division 1",
        }
    ],
    employee_id="employeeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

ID of an Employee for whom you want to update the custom field

##### requestBody: [`EmployeeCustomFieldsUpdateByEmployeeIdRequest`](./paycor_python_sdk/type/employee_custom_fields_update_by_employee_id_request.py)<a id="requestbody-employeecustomfieldsupdatebyemployeeidrequestpaycor_python_sdktypeemployee_custom_fields_update_by_employee_id_requestpy"></a>

CustomFields object

#### 🔄 Return<a id="🔄-return"></a>

[`CreateOrUpdateResponse`](./paycor_python_sdk/pydantic/create_or_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/customfields` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_deductions.add_deduction_to_employee`<a id="paycoremployee_deductionsadd_deduction_to_employee"></a>

Tip: first call "Get Legal Entity Deductions by Legal Entity ID" to get the valid Deduction Codes

Data Access: Add Employee Deduction

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_deduction_to_employee_response = paycor.employee_deductions.add_deduction_to_employee(
    code="Pension",
    employee_id="employeeId_example",
    on_hold=True,
    frequency="EveryPayPeriod",
    include_in_pay="AddtlPayOnly",
    amount_data=[
        {
            "rate": 0.58,
            "amount": 3141.59,
            "effective_start_date": "2019-11-01T00:00:00Z",
            "effective_end_date": "2020-11-01T00:00:00Z",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

Unique deduction code set at the legal entity or tenant level.  

##### employee_id: `str`<a id="employee_id-str"></a>

ID of an Employee for whom you want to add the deduction

##### on_hold: `bool`<a id="on_hold-bool"></a>

Specifies whether the deduction should be deducted in a paycheck.             

##### frequency: [`PayFrequency`](./paycor_python_sdk/type/pay_frequency.py)<a id="frequency-payfrequencypaycor_python_sdktypepay_frequencypy"></a>

##### include_in_pay: [`IncludeInPay`](./paycor_python_sdk/type/include_in_pay.py)<a id="include_in_pay-includeinpaypaycor_python_sdktypeinclude_in_paypy"></a>

##### amount_data: List[`EmployeeDeductionAmount2`]<a id="amount_data-listemployeedeductionamount2"></a>

Specifies the rate and amount for the employee deduction.             

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeDeduction2`](./paycor_python_sdk/type/employee_deduction2.py)
EmployeeDeduction object

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeDeductionsAddDeductionToEmployeeResponse`](./paycor_python_sdk/pydantic/employee_deductions_add_deduction_to_employee_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/deductions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_deductions.get_by_employee_id`<a id="paycoremployee_deductionsget_by_employee_id"></a>

Data Access: View Employee Deductions Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_employee_id_response = paycor.employee_deductions.get_by_employee_id(
    employee_id="employeeId_example",
    include=[
        "string_example"
    ],
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

ID of the employee for whom you want to get the deductions

##### include: List[[`Includes4`](./paycor_python_sdk/type/includes4.py)]<a id="include-listincludes4paycor_python_sdktypeincludes4py"></a>

Options to include more data: All, AmountData  Data Access required  AmountData = View Employee Deductions Amounts

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get the next set of employee earnings

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfEmployeeDeduction`](./paycor_python_sdk/pydantic/paged_result_of_employee_deduction.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/deductions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_deductions.get_by_employee_id_and_deduction_id`<a id="paycoremployee_deductionsget_by_employee_id_and_deduction_id"></a>

Data Access: View Employee Deduction Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_employee_id_and_deduction_id_response = paycor.employee_deductions.get_by_employee_id_and_deduction_id(
    employee_id="employeeId_example",
    employee_deduction_id="employeeDeductionId_example",
    include=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

ID of an Employee for whom you want to get the deduction.

##### employee_deduction_id: `str`<a id="employee_deduction_id-str"></a>

ID of the Employee Deduction you want to get.

##### include: List[[`Includes3`](./paycor_python_sdk/type/includes3.py)]<a id="include-listincludes3paycor_python_sdktypeincludes3py"></a>

Options to include more data: All, AmountData  Data Access required  AmountData = View Employee Deduction Amounts

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeDeduction`](./paycor_python_sdk/pydantic/employee_deduction.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/deductions/{employeeDeductionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_deductions.update_by_employee_id`<a id="paycoremployee_deductionsupdate_by_employee_id"></a>

Data Access: Update Employee Deduction

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_employee_id_response = paycor.employee_deductions.update_by_employee_id(
    id="a",
    employee_id="employeeId_example",
    include_in_pay="AddtlPayOnly",
    frequency="EveryPayPeriod",
    on_hold=True,
    amount_data=[
        {
            "rate": 0.58,
            "amount": 3141.59,
            "effective_start_date": "2019-11-01T00:00:00Z",
            "effective_end_date": "2020-11-01T00:00:00Z",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The unique identifier of this employee deduction generated in Paycor's system. Used as the Key for Update (PUT) endpoint. 

##### employee_id: `str`<a id="employee_id-str"></a>

ID of an Employee that has the Deduction you wish to update

##### include_in_pay: [`IncludeInPay`](./paycor_python_sdk/type/include_in_pay.py)<a id="include_in_pay-includeinpaypaycor_python_sdktypeinclude_in_paypy"></a>

##### frequency: [`PayFrequency`](./paycor_python_sdk/type/pay_frequency.py)<a id="frequency-payfrequencypaycor_python_sdktypepay_frequencypy"></a>

##### on_hold: `Optional[bool]`<a id="on_hold-optionalbool"></a>

Specifies whether the deduction should be deducted in a paycheck. Required, defaults to false (meaning it should be deducted).             

##### amount_data: List[`EmployeeDeductionAmount3`]<a id="amount_data-listemployeedeductionamount3"></a>

Specifies the rate and amount for the employee deduction.             

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeDeduction3`](./paycor_python_sdk/type/employee_deduction3.py)
EmployeeDeduction with ID set and fields updated

#### 🔄 Return<a id="🔄-return"></a>

[`CreateOrUpdateResponse`](./paycor_python_sdk/pydantic/create_or_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/deductions` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_direct_deposits.add_by_employee_id`<a id="paycoremployee_direct_depositsadd_by_employee_id"></a>

Data Access: Add Employee Direct Deposit

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_by_employee_id_response = paycor.employee_direct_deposits.add_by_employee_id(
    account_type="Checking",
    frequency="EveryPayPeriod",
    on_hold=True,
    employee_id="employeeId_example",
    account_number="1234567890",
    routing_number="322271627",
    deduction_code="string_example",
    direct_deposit_type="Net",
    amount=22.22,
    rate=0.84,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_type: [`AccountType`](./paycor_python_sdk/type/account_type.py)<a id="account_type-accounttypepaycor_python_sdktypeaccount_typepy"></a>

##### frequency: [`PayFrequency`](./paycor_python_sdk/type/pay_frequency.py)<a id="frequency-payfrequencypaycor_python_sdktypepay_frequencypy"></a>

##### on_hold: `bool`<a id="on_hold-bool"></a>

Whether any money should be deposited into the direct deposit account.

##### employee_id: `str`<a id="employee_id-str"></a>

Id of employee for which you want to add Direct Deposits

##### account_number: `Optional[str]`<a id="account_number-optionalstr"></a>

The bank account number where the direct deposit is directed.             

##### routing_number: `Optional[str]`<a id="routing_number-optionalstr"></a>

The bank routing number where the direct deposit is directed.              

##### deduction_code: `Optional[str]`<a id="deduction_code-optionalstr"></a>

##### direct_deposit_type: [`DirectDepositType`](./paycor_python_sdk/type/direct_deposit_type.py)<a id="direct_deposit_type-directdeposittypepaycor_python_sdktypedirect_deposit_typepy"></a>

##### amount: `Optional[Union[int, float]]`<a id="amount-optionalunionint-float"></a>

Fixed, recurring dollar amount.             

##### rate: `Optional[Union[int, float]]`<a id="rate-optionalunionint-float"></a>

Percentage of the paycheck to be deposited into the direct deposit account             

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeDirectDeposit2`](./paycor_python_sdk/type/employee_direct_deposit2.py)
Direct Deposit object to insert

#### 🔄 Return<a id="🔄-return"></a>

[`CreateOrUpdateResponse`](./paycor_python_sdk/pydantic/create_or_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/DirectDeposits` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_direct_deposits.add_by_employee_id_hsa`<a id="paycoremployee_direct_depositsadd_by_employee_id_hsa"></a>

Data Access: Add Employee HSA Account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_by_employee_id_hsa_response = paycor.employee_direct_deposits.add_by_employee_id_hsa(
    account_type="Checking",
    frequency="EveryPayPeriod",
    deduction_code="Pension",
    on_hold=True,
    employee_id="employeeId_example",
    account_number="1234567890",
    routing_number="322271627",
    amount=22.22,
    rate=0.84,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_type: [`AccountType`](./paycor_python_sdk/type/account_type.py)<a id="account_type-accounttypepaycor_python_sdktypeaccount_typepy"></a>

##### frequency: [`PayFrequency`](./paycor_python_sdk/type/pay_frequency.py)<a id="frequency-payfrequencypaycor_python_sdktypepay_frequencypy"></a>

##### deduction_code: `str`<a id="deduction_code-str"></a>

Unique deduction code set at the legal entity or tenant level.  

##### on_hold: `bool`<a id="on_hold-bool"></a>

Whether any money should be deposited into the HSA direct deposit account.

##### employee_id: `str`<a id="employee_id-str"></a>

ID of employee for which you want to add HSA Direct Deposits

##### account_number: `Optional[str]`<a id="account_number-optionalstr"></a>

The bank account number where the HSA direct deposit is directed.             

##### routing_number: `Optional[str]`<a id="routing_number-optionalstr"></a>

The bank routing number where the HSA direct deposit is directed.              

##### amount: `Optional[Union[int, float]]`<a id="amount-optionalunionint-float"></a>

Fixed, recurring dollar amount.             

##### rate: `Optional[Union[int, float]]`<a id="rate-optionalunionint-float"></a>

Percentage of the paycheck to be deposited into the HSA direct deposit account             

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeHsaDirectDeposit`](./paycor_python_sdk/type/employee_hsa_direct_deposit.py)
HSA Direct Deposit object to insert

#### 🔄 Return<a id="🔄-return"></a>

[`CreateOrUpdateResponse`](./paycor_python_sdk/pydantic/create_or_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/HSAaccounts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_direct_deposits.get_by_employee_and_deposit_id`<a id="paycoremployee_direct_depositsget_by_employee_and_deposit_id"></a>

Data Access: View Employee Direct Deposit Information by Direct Deposit Id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_employee_and_deposit_id_response = paycor.employee_direct_deposits.get_by_employee_and_deposit_id(
    employee_id="employeeId_example",
    direct_deposit_id="directDepositId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

ID of employee for which you want to get Direct Deposits

##### direct_deposit_id: `str`<a id="direct_deposit_id-str"></a>

ID of an employee direct deposit which you want to retrieve

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeDirectDeposit`](./paycor_python_sdk/pydantic/employee_direct_deposit.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/DirectDeposits/{directDepositId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_direct_deposits.get_by_employee_id`<a id="paycoremployee_direct_depositsget_by_employee_id"></a>

Data Access: View Employee Direct Deposit Information by Employee Id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_employee_id_response = paycor.employee_direct_deposits.get_by_employee_id(
    employee_id="employeeId_example",
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

ID of employee for which you want to get Direct Deposits

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get next set of direct deposits

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfEmployeeDirectDeposit`](./paycor_python_sdk/pydantic/paged_result_of_employee_direct_deposit.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/DirectDeposits` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_direct_deposits.get_by_employee_id_hsa`<a id="paycoremployee_direct_depositsget_by_employee_id_hsa"></a>

Data Access: View Employee HSA Account Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_employee_id_hsa_response = paycor.employee_direct_deposits.get_by_employee_id_hsa(
    employee_id="employeeId_example",
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

ID of employee for whom you want to get HSA Direct Deposits

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get next set of HSA Direct Deposits

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfEmployeeDirectDeposit`](./paycor_python_sdk/pydantic/paged_result_of_employee_direct_deposit.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/HSAaccounts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_direct_deposits.update_by_employee_id_ddd`<a id="paycoremployee_direct_depositsupdate_by_employee_id_ddd"></a>

Data Access: Update Employee Direct Deposit Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_employee_id_ddd_response = paycor.employee_direct_deposits.update_by_employee_id_ddd(
    id="5e699a0d-0000-0000-0000-0007d54d9839",
    account_type="Checking",
    account_number="1234567890",
    routing_number="322271627",
    frequency="EveryPayPeriod",
    on_hold=True,
    employee_id="employeeId_example",
    direct_deposit_type="Net",
    amount=22.22,
    rate=0.84,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Unique identifier of the employee direct deposit in Paycor's system. Generated by Paycor.             

##### account_type: [`AccountType`](./paycor_python_sdk/type/account_type.py)<a id="account_type-accounttypepaycor_python_sdktypeaccount_typepy"></a>

##### account_number: `str`<a id="account_number-str"></a>

The bank account number where the direct deposit is directed.             

##### routing_number: `str`<a id="routing_number-str"></a>

The bank routing number where the direct deposit is directed.              

##### frequency: [`PayFrequency`](./paycor_python_sdk/type/pay_frequency.py)<a id="frequency-payfrequencypaycor_python_sdktypepay_frequencypy"></a>

##### on_hold: `bool`<a id="on_hold-bool"></a>

Whether any money should be deposited into the direct deposit account.

##### employee_id: `str`<a id="employee_id-str"></a>

ID of employee for which you want to update Direct Deposit

##### direct_deposit_type: [`DirectDepositType`](./paycor_python_sdk/type/direct_deposit_type.py)<a id="direct_deposit_type-directdeposittypepaycor_python_sdktypedirect_deposit_typepy"></a>

##### amount: `Optional[Union[int, float]]`<a id="amount-optionalunionint-float"></a>

Fixed, recurring dollar amount.             

##### rate: `Optional[Union[int, float]]`<a id="rate-optionalunionint-float"></a>

Percentage of the paycheck to be deposited into the direct deposit account             

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeDirectDeposit3`](./paycor_python_sdk/type/employee_direct_deposit3.py)
Employee Direct Deposit object with updated fields

#### 🔄 Return<a id="🔄-return"></a>

[`CreateOrUpdateResponse`](./paycor_python_sdk/pydantic/create_or_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/DirectDeposits` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_direct_deposits.update_hsa_direct_deposits_by_employee_id`<a id="paycoremployee_direct_depositsupdate_hsa_direct_deposits_by_employee_id"></a>

Data Access: Update Employee HSA Account Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_hsa_direct_deposits_by_employee_id_response = paycor.employee_direct_deposits.update_hsa_direct_deposits_by_employee_id(
    id="5e699a0d-0000-0000-0000-0007d54d9839",
    account_type="Checking",
    account_number="1234567890",
    routing_number="322271627",
    frequency="EveryPayPeriod",
    on_hold=True,
    employee_id="employeeId_example",
    amount=22.22,
    rate=0.84,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Unique identifier of the employee hsa direct deposit in Paycor's system. Generated by Paycor.             

##### account_type: [`AccountType`](./paycor_python_sdk/type/account_type.py)<a id="account_type-accounttypepaycor_python_sdktypeaccount_typepy"></a>

##### account_number: `str`<a id="account_number-str"></a>

The bank account number where the HSA direct deposit is directed.             

##### routing_number: `str`<a id="routing_number-str"></a>

The bank routing number where the HSA direct deposit is directed.              

##### frequency: [`PayFrequency`](./paycor_python_sdk/type/pay_frequency.py)<a id="frequency-payfrequencypaycor_python_sdktypepay_frequencypy"></a>

##### on_hold: `bool`<a id="on_hold-bool"></a>

Whether any money should be deposited into the HSA direct deposit account.

##### employee_id: `str`<a id="employee_id-str"></a>

ID of employee for which you want to update HSA Direct Deposits

##### amount: `Optional[Union[int, float]]`<a id="amount-optionalunionint-float"></a>

Fixed, recurring dollar amount.             

##### rate: `Optional[Union[int, float]]`<a id="rate-optionalunionint-float"></a>

Percentage of the paycheck to be deposited into the HSA direct deposit account             

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeHsaDirectDeposit2`](./paycor_python_sdk/type/employee_hsa_direct_deposit2.py)
HSA Employee Direct Deposit object with updated fields

#### 🔄 Return<a id="🔄-return"></a>

[`CreateOrUpdateResponse`](./paycor_python_sdk/pydantic/create_or_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/HSAaccounts` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_documents.download_pay_stub`<a id="paycoremployee_documentsdownload_pay_stub"></a>

Data Access: Download Employee Pay Stub Document

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
download_pay_stub_response = paycor.employee_documents.download_pay_stub(
    employee_id="employeeId_example",
    document_id="documentId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

Id of an Employee for whom you want to get the Pay Stub Document

##### document_id: `str`<a id="document_id-str"></a>

Id of Pay Stub Document

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/PayStubDocument/{documentId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_documents.get_pay_stub_document_by_employee_id`<a id="paycoremployee_documentsget_pay_stub_document_by_employee_id"></a>

Start Date and End Date are required parameters.

Data Access: Get Employee Pay Stub Document Link

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_pay_stub_document_by_employee_id_response = paycor.employee_documents.get_pay_stub_document_by_employee_id(
    employee_id="employeeId_example",
    start_date="1970-01-01T00:00:00.00Z",
    end_date="1970-01-01T00:00:00.00Z",
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

ID of an Employee for whom you want to get the Pay Stubs Document Link

##### start_date: `datetime`<a id="start_date-datetime"></a>

Date that is earlier or equal to paycheck date

##### end_date: `datetime`<a id="end_date-datetime"></a>

Date that is after or equal to paycheck date

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get the next set of Employee Pay Stubs Document Links

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfPayStubFile`](./paycor_python_sdk/pydantic/paged_result_of_pay_stub_file.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/paystubDocumentData` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_earnings.add_new_earning`<a id="paycoremployee_earningsadd_new_earning"></a>

Data Access: Add Employee Earning

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_new_earning_response = paycor.employee_earnings.add_new_earning(
    code="BonusDis",
    amount_data=[
        {
            "rate": 55.55,
            "amount": 5555.55,
            "factor": 1,
            "effective_start_date": "2019-12-01T00:00:00Z",
            "effective_end_date": "2020-11-01T00:00:00Z",
        }
    ],
    employee_id="employeeId_example",
    frequency="EveryPayPeriod",
    sequence_number=3,
    include_in_pay="AddtlPayOnly",
    on_hold=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

Descriptive earning identifier which appears on paychecks. Only set at the legal entity or tenant level.

##### amount_data: List[`EmployeeEarningAmount`]<a id="amount_data-listemployeeearningamount"></a>

List of the employee's earning rates, factors and amounts of type EmployeeEarningAmount.             

##### employee_id: `str`<a id="employee_id-str"></a>

ID of an Employee for whom you want to add an Earning

##### frequency: [`PayFrequency`](./paycor_python_sdk/type/pay_frequency.py)<a id="frequency-payfrequencypaycor_python_sdktypepay_frequencypy"></a>

##### sequence_number: `Optional[int]`<a id="sequence_number-optionalint"></a>

Order earnings are calculated based on sequence values. This is needed so earnings dependent on other earnings are calculated in the proper sequence.

##### include_in_pay: [`IncludeInPay`](./paycor_python_sdk/type/include_in_pay.py)<a id="include_in_pay-includeinpaypaycor_python_sdktypeinclude_in_paypy"></a>

##### on_hold: `bool`<a id="on_hold-bool"></a>

Whether the employee earning should included in a paycheck. This is specified by the 'Calculate' checkbox in the Paycor UI.             

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeEarning2`](./paycor_python_sdk/type/employee_earning2.py)
Employee Earning object to insert

#### 🔄 Return<a id="🔄-return"></a>

[`CreateOrUpdateResponse`](./paycor_python_sdk/pydantic/create_or_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/earnings` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_earnings.get_by_employee_and_earning`<a id="paycoremployee_earningsget_by_employee_and_earning"></a>

Data Access: View Employee Earning Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_employee_and_earning_response = paycor.employee_earnings.get_by_employee_and_earning(
    employee_id="employeeId_example",
    employee_earning_id="employeeEarningId_example",
    include=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

ID of an Employee for whom you want to get the Earning

##### employee_earning_id: `str`<a id="employee_earning_id-str"></a>

ID of an Employee Earning you want to get

##### include: List[[`Includes5`](./paycor_python_sdk/type/includes5.py)]<a id="include-listincludes5paycor_python_sdktypeincludes5py"></a>

Options to include more data: All, AmountData  Data Access required  AmountData = View Employee Earning Amounts

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeEarning`](./paycor_python_sdk/pydantic/employee_earning.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/earnings/{employeeEarningId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_earnings.get_by_employee_id`<a id="paycoremployee_earningsget_by_employee_id"></a>

Data Access: View Employee Earnings Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_employee_id_response = paycor.employee_earnings.get_by_employee_id(
    employee_id="employeeId_example",
    include=[
        "string_example"
    ],
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

ID of an Employee for whom you want to get the Earnings

##### include: List[[`Includes6`](./paycor_python_sdk/type/includes6.py)]<a id="include-listincludes6paycor_python_sdktypeincludes6py"></a>

Options to include more data: All, AmountData  Data Access required  AmountData = View Employee Earnings Amounts

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get the next set of Employee Earnings

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfEmployeeEarning`](./paycor_python_sdk/pydantic/paged_result_of_employee_earning.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/earnings` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_earnings.update_data`<a id="paycoremployee_earningsupdate_data"></a>

Data Access: Update Employee Earning

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_data_response = paycor.employee_earnings.update_data(
    id="a",
    code="BonusDis",
    frequency="EveryPayPeriod",
    include_in_pay="AddtlPayOnly",
    on_hold=False,
    amount_data=[
        {
            "rate": 55.55,
            "amount": 5555.55,
            "factor": 1,
            "effective_start_date": "2019-12-01T00:00:00Z",
            "effective_end_date": "2020-11-01T00:00:00Z",
        }
    ],
    employee_id="employeeId_example",
    sequence_number=3,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The unique identifier of this employee earning generated in Paycor's system.

##### code: `str`<a id="code-str"></a>

Descriptive earning identifier which appears on paychecks. Only set at the legal entity or tenant level.

##### frequency: [`PayFrequency`](./paycor_python_sdk/type/pay_frequency.py)<a id="frequency-payfrequencypaycor_python_sdktypepay_frequencypy"></a>

##### include_in_pay: [`IncludeInPay`](./paycor_python_sdk/type/include_in_pay.py)<a id="include_in_pay-includeinpaypaycor_python_sdktypeinclude_in_paypy"></a>

##### on_hold: `bool`<a id="on_hold-bool"></a>

Whether the employee earning should included in a paycheck. This is specified by the 'Calculate' checkbox in the Paycor UI.             

##### amount_data: List[`EmployeeEarningAmount`]<a id="amount_data-listemployeeearningamount"></a>

List of the employee's earning rates, factors and amounts of type EmployeeEarningAmount.             

##### employee_id: `str`<a id="employee_id-str"></a>

ID of an Employee that has the Earning you wish to update

##### sequence_number: `Optional[int]`<a id="sequence_number-optionalint"></a>

Order earnings are calculated based on sequence values. This is needed so earnings dependent on other earnings are calculated in the proper sequence.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeEarning3`](./paycor_python_sdk/type/employee_earning3.py)
Employee Earning object with updated fields

#### 🔄 Return<a id="🔄-return"></a>

[`CreateOrUpdateResponse`](./paycor_python_sdk/pydantic/create_or_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/earnings` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_emergency_contact.create_update`<a id="paycoremployee_emergency_contactcreate_update"></a>

Either Home Phone, Work Phone or Mobile Phone must be specified

Data Access: Create Emergency Contact

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_update_response = paycor.employee_emergency_contact.create_update(
    first_name="Charles",
    last_name="Dodgson",
    employee_id="employeeId_example",
    middle_name="Lutwidge",
    relationship="Daughter",
    home_phone="1234567890",
    work_phone="1234567890",
    work_phone_extension="123",
    mobile_phone="1234567890",
    email_address="abc@paycor.com",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### first_name: `str`<a id="first_name-str"></a>

First name of the emergency contact.

##### last_name: `str`<a id="last_name-str"></a>

Last name of the emergency contact.

##### employee_id: `str`<a id="employee_id-str"></a>

##### middle_name: `Optional[str]`<a id="middle_name-optionalstr"></a>

Middle name of the emergency contact.

##### relationship: [`Relationship`](./paycor_python_sdk/type/relationship.py)<a id="relationship-relationshippaycor_python_sdktyperelationshippy"></a>

##### home_phone: `Optional[str]`<a id="home_phone-optionalstr"></a>

Home Phone of the emergency contact. Must be 10 characters.             

##### work_phone: `Optional[str]`<a id="work_phone-optionalstr"></a>

Work Phone of the emergency contact. Must be 10 characters.             

##### work_phone_extension: `Optional[str]`<a id="work_phone_extension-optionalstr"></a>

Work Phone extension of the emergency contact.             

##### mobile_phone: `Optional[str]`<a id="mobile_phone-optionalstr"></a>

Mobile Phone of the emergency contact. Must be 10 characters.             

##### email_address: `Optional[str]`<a id="email_address-optionalstr"></a>

Email Address of the emergency contact.             

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmergencyContact`](./paycor_python_sdk/type/emergency_contact.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CreateOrUpdateResponse`](./paycor_python_sdk/pydantic/create_or_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/emergencycontact` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_i9_verification.get_by_employee_id`<a id="paycoremployee_i9_verificationget_by_employee_id"></a>

Data Access: View I9 Verification

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_employee_id_response = paycor.employee_i9_verification.get_by_employee_id(
    employee_id="employeeId_example",
    include=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

ID of the employee for whom you want to get the I9 information

##### include: List[[`Includes7`](./paycor_python_sdk/type/includes7.py)]<a id="include-listincludes7paycor_python_sdktypeincludes7py"></a>

Options to include more data: documents

#### 🔄 Return<a id="🔄-return"></a>

[`I9Verification`](./paycor_python_sdk/pydantic/i9_verification.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/I9Verification` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_i9_verification.update_by_employee_id_i9_verification`<a id="paycoremployee_i9_verificationupdate_by_employee_id_i9_verification"></a>

Data Access: Edit I9 Verification

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_employee_id_i9_verification_response = paycor.employee_i9_verification.update_by_employee_id_i9_verification(
    employee_id="employeeId_example",
    citizen_of_country="USA",
    work_eligibility="USCitizen",
    work_visa_type="H1B",
    work_visa_expiration_date="10/25/2023",
    alien_admission_number="12365478961",
    alien_admission_expiration_date="05/25/2023",
    list_a={
        "document_title": "USPassport",
        "document_number": "1234567",
        "issuing_authority": "state",
        "list_expiration_date": "01/01/2020",
    },
    list_b={
        "document_title": "DriverLicenseorIDcard",
        "document_number": "1234567",
        "issuing_authority": "state",
        "list_expiration_date": "01/01/2020",
    },
    list_c={
        "document_title": "SocialSecurityAccountNumber",
        "document_number": "1234567",
        "issuing_authority": "state",
        "list_expiration_date": "01/01/2020",
    },
    foreign_passport_number="N4123456",
    country_of_issuance="AU",
    additional_information="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

ID of an Employee for whom you want to update the I9 Verification

##### citizen_of_country: `Optional[str]`<a id="citizen_of_country-optionalstr"></a>

Country of which the employee is citizen of.             

##### work_eligibility: [`WorkEligibility`](./paycor_python_sdk/type/work_eligibility.py)<a id="work_eligibility-workeligibilitypaycor_python_sdktypework_eligibilitypy"></a>

##### work_visa_type: `Optional[str]`<a id="work_visa_type-optionalstr"></a>

Work visa type of the employee. Maximum characters should be 20.             

##### work_visa_expiration_date: `Optional[datetime]`<a id="work_visa_expiration_date-optionaldatetime"></a>

Expiration date of the work visa.             

##### alien_admission_number: `Optional[str]`<a id="alien_admission_number-optionalstr"></a>

Alien admission number of the employee.             

##### alien_admission_expiration_date: `Optional[datetime]`<a id="alien_admission_expiration_date-optionaldatetime"></a>

Expiration date of the alien admission.             

##### list_a: [`ListA`](./paycor_python_sdk/type/list_a.py)<a id="list_a-listapaycor_python_sdktypelist_apy"></a>


##### list_b: [`ListB`](./paycor_python_sdk/type/list_b.py)<a id="list_b-listbpaycor_python_sdktypelist_bpy"></a>


##### list_c: [`ListC`](./paycor_python_sdk/type/list_c.py)<a id="list_c-listcpaycor_python_sdktypelist_cpy"></a>


##### foreign_passport_number: `Optional[str]`<a id="foreign_passport_number-optionalstr"></a>

Foreign passport number of the employee.             

##### country_of_issuance: `Optional[str]`<a id="country_of_issuance-optionalstr"></a>

Country of issuance of the foreign passport. Accepted values ISO-3166 alpha2 or alpha3 codes for countries.             

##### additional_information: `Optional[str]`<a id="additional_information-optionalstr"></a>

Additional information for the I9 verification. Must be under 768 characters.             

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`I9Verification2`](./paycor_python_sdk/type/i9_verification2.py)
I9 Verification object

#### 🔄 Return<a id="🔄-return"></a>

[`CreateOrUpdateResponse`](./paycor_python_sdk/pydantic/create_or_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/I9Verification` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_onboarding.add_new_entry`<a id="paycoremployee_onboardingadd_new_entry"></a>

This will allow partners to add a new employee entry for pending hire

Data Access: Create Employee Onboarding

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_new_entry_response = paycor.employee_onboarding.add_new_entry(
    legal_entity_id=122900,
    first_name="Edwin",
    last_name="Hubble",
    home_email_address="homeEmail@domain.com",
    exported_by_email_address="email@domain.com",
    preferred_name="Carroll",
    country_code="USA",
    zip="45212",
    state="OH",
    city="Cincinnati",
    address1="4811 Montgomery Road",
    address2="Building A",
    mobile_phone="(123) 456–7890",
    home_phone="(123) 456–7890",
    gender="Male",
    ethnicity="AmerIndorAKNative",
    veteran_status="true",
    start_date="2019-11-01T00:00:00Z",
    job_title="Software Engineer",
    department_code="80",
    disability="true",
    base_salary=10000,
    salary_frequency="Bi-Weekly",
    work_location_id="dc069074-24b2-0000-0000-000014e00100",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

Legal Entity Id

##### first_name: `str`<a id="first_name-str"></a>

First name of the person. 

##### last_name: `str`<a id="last_name-str"></a>

Last name of the person.

##### home_email_address: `str`<a id="home_email_address-str"></a>

Email Information of the person.             

##### exported_by_email_address: `Optional[str]`<a id="exported_by_email_address-optionalstr"></a>

Email of the user exporting records

##### preferred_name: `Optional[str]`<a id="preferred_name-optionalstr"></a>

Preferred Name of the Person             

##### country_code: `Optional[str]`<a id="country_code-optionalstr"></a>

Country in the address.             

##### zip: `Optional[str]`<a id="zip-optionalstr"></a>

Zip code in the address.             

##### state: `Optional[str]`<a id="state-optionalstr"></a>

State in the address.             

##### city: `Optional[str]`<a id="city-optionalstr"></a>

City in the address.             

##### address1: `Optional[str]`<a id="address1-optionalstr"></a>

First line of street address information.             

##### address2: `Optional[str]`<a id="address2-optionalstr"></a>

Additional line of street address information.             

##### mobile_phone: `Optional[str]`<a id="mobile_phone-optionalstr"></a>

Mobile phone number. 

##### home_phone: `Optional[str]`<a id="home_phone-optionalstr"></a>

Home phone number. 

##### gender: [`Gender`](./paycor_python_sdk/type/gender.py)<a id="gender-genderpaycor_python_sdktypegenderpy"></a>

##### ethnicity: [`EthnicityType`](./paycor_python_sdk/type/ethnicity_type.py)<a id="ethnicity-ethnicitytypepaycor_python_sdktypeethnicity_typepy"></a>

##### veteran_status: [`VeteranStatus`](./paycor_python_sdk/type/veteran_status.py)<a id="veteran_status-veteranstatuspaycor_python_sdktypeveteran_statuspy"></a>

##### start_date: `datetime`<a id="start_date-datetime"></a>

Date the employement start. Format: YYYY-MM-DDTHH:MM:SSZ  (ISO-8601 standard)              

##### job_title: `Optional[str]`<a id="job_title-optionalstr"></a>

Name of the Job Title to associate with new hire.             

##### department_code: `Optional[str]`<a id="department_code-optionalstr"></a>

Code of the department in Paycor's system.  Can be retrieved by calling 'Get Legal Entity Departments by Legal Entity ID'

##### disability: [`DisabilityStatus`](./paycor_python_sdk/type/disability_status.py)<a id="disability-disabilitystatuspaycor_python_sdktypedisability_statuspy"></a>

##### base_salary: `Optional[Union[int, float]]`<a id="base_salary-optionalunionint-float"></a>

Base Salary of new hire employee

##### salary_frequency: `Optional[str]`<a id="salary_frequency-optionalstr"></a>

Salary Frequency of new hire employee

##### work_location_id: `Optional[str]`<a id="work_location_id-optionalstr"></a>

Worklocation Id of new hire employee

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SimpleHire`](./paycor_python_sdk/type/simple_hire.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CreateOrUpdateResponse`](./paycor_python_sdk/pydantic/create_or_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/onboarding` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_onboarding.list_onboarding_employees`<a id="paycoremployee_onboardinglist_onboarding_employees"></a>

This endpoint allows partners to see the employees in the onboarding state.

Data Access: View Legal Entity Onboarding Employees

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_onboarding_employees_response = paycor.employee_onboarding.list_onboarding_employees(
    legal_entity_id=1,
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of the legal entity for which you want to get the employees in the onboarding state

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get next set of Onboarding Employee records

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfOnboardingEmployee`](./paycor_python_sdk/pydantic/paged_result_of_onboarding_employee.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/onboardingemployees` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_pay_rates.add_new_rate`<a id="paycoremployee_pay_ratesadd_new_rate"></a>

This immediately creates a new payrate related to an Employee in Paycor's system. There is no way to undo or reverse this operation. 

Data Access: Create Employee PayRates
Sequence numbers must be consecutive and unique

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_new_rate_response = paycor.employee_pay_rates.add_new_rate(
    effective_start_date="2019-11-22T00:00:00Z",
    sequence_number=1,
    description="Rate 1",
    employee_id="employeeId_example",
    effective_end_date="2020-12-01T12:15:00Z",
    pay_rate=25.52,
    annual_pay_rate=53081.6,
    type="Salary",
    reason="Merit Increase.",
    notes="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_start_date: `datetime`<a id="effective_start_date-datetime"></a>

Represents the date that the payrate goes into effect.  You can pass in future dates to take effect in future, or today's date to take effect immediately.  Format: YYYY-MM-DDTHH:MM:SSZ  (ISO-8601 standard)              

##### sequence_number: `int`<a id="sequence_number-int"></a>

Orders how multiple earnings are calculated. Needed so earnings dependent on other earnings are calculated in the proper sequence. Must be unique and be ascending without gaps (ie 1, 2, 3…). Use GET Payrates to identify existing sequences.

##### description: `str`<a id="description-str"></a>

Required. Brief description of the employee's pay rate. Defaults to \\\"Rate {SequenceNumber}\\\" Must be 20 characters or less             

##### employee_id: `str`<a id="employee_id-str"></a>

ID of the Employee you wish to create the payrate for

##### effective_end_date: `Optional[datetime]`<a id="effective_end_date-optionaldatetime"></a>

Date when the employee pay rate is no longer in effect. Default to null. Only pass in a date if the payrate is no longer active. Format: YYYY-MM-DDTHH:MM:SSZ  (ISO-8601 standard)              

##### pay_rate: `Optional[Union[int, float]]`<a id="pay_rate-optionalunionint-float"></a>

Employee's rate of pay (in dollars).  If Pay Type is Hourly, then Pay Rate is a Per-Hour dollar amount and is required.  If Pay Type is Salary, then Pay Rate is a Per-Pay dollar amount, and either Pay Rate or Annual Rate is required. Payrate can't have more than 6 decimal places and can't be negative.              

##### annual_pay_rate: `Optional[Union[int, float]]`<a id="annual_pay_rate-optionalunionint-float"></a>

Employee's annual pay amount (in dollars). Only used if Type=Salary.  * For Salary Type, AnnualPayRate overrides payRate if passed into API call. The value not provided will be calculated based on Employee's Annual Hours setup on Employee's Profile. * For Hourly Type, this parameter is ignored - Paycor calculates based on Employee's Annual Hours setup on Employee's Profile.             

##### type: [`PayType`](./paycor_python_sdk/type/pay_type.py)<a id="type-paytypepaycor_python_sdktypepay_typepy"></a>

##### reason: `Optional[str]`<a id="reason-optionalstr"></a>

Reason associated with the employee's pay rate. Optional.              

##### notes: `Optional[str]`<a id="notes-optionalstr"></a>

Notes associated with the employee's pay rate, which will be displayed on Pay Rate History page.  Must be 512 characters or less. Optional.              

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeePayRate2`](./paycor_python_sdk/type/employee_pay_rate2.py)
Create Payrate model

#### 🔄 Return<a id="🔄-return"></a>

[`CreateOrUpdateResponse`](./paycor_python_sdk/pydantic/create_or_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/payrates` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_pay_rates.get_by_employee_id`<a id="paycoremployee_pay_ratesget_by_employee_id"></a>

Data Access: View Employee Payrates

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_employee_id_response = paycor.employee_pay_rates.get_by_employee_id(
    employee_id="employeeId_example",
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

ID of employee for which you want to get payrates

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get next set of payrates

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfEmployeePayRate`](./paycor_python_sdk/pydantic/paged_result_of_employee_pay_rate.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/payrates` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_pay_rates.update_by_employee_id_and_payrate_id`<a id="paycoremployee_pay_ratesupdate_by_employee_id_and_payrate_id"></a>

Data Access: Update Employee PayRates

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_employee_id_and_payrate_id_response = paycor.employee_pay_rates.update_by_employee_id_and_payrate_id(
    effective_start_date="2019-11-22T00:00:00Z",
    pay_rate=25.52,
    description="Rate 1",
    employee_id="employeeId_example",
    payrate_id="payrateId_example",
    sequence_number=1,
    annual_pay_rate=53081.6,
    type="Salary",
    reason="Merit Increase.",
    notes="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_start_date: `datetime`<a id="effective_start_date-datetime"></a>

Represents the date that the payrate goes into effect.  PUT requires EffectiveStartDate value to be unique for this PayRateId.              

##### pay_rate: `Union[int, float]`<a id="pay_rate-unionint-float"></a>

Employee's rate of pay (in dollars).  If Pay Type is Hourly, then Pay Rate is a Per-Hour dollar amount and is required.  If Pay Type is Salary, then Pay Rate is a Per-Pay dollar amount, and either Pay Rate or Annual Rate is required. Payrate can't have more than 6 decimal places and can't be negative.              

##### description: `str`<a id="description-str"></a>

Required. Brief description of the employee's pay rate. Defaults to \\\"Rate {SequenceNumber}\\\" Must be 20 characters or less             

##### employee_id: `str`<a id="employee_id-str"></a>

ID of an Employee that has the Payrate you wish to update

##### payrate_id: `str`<a id="payrate_id-str"></a>

ID of the Payrate you wish to update

##### sequence_number: `int`<a id="sequence_number-int"></a>

Orders how multiple earnings are calculated. Needed so earnings dependent on other earnings are calculated in the proper sequence. For PUT, this should match an existing SequenceNumber (retrieved via GET Employee PayRates).

##### annual_pay_rate: `Optional[Union[int, float]]`<a id="annual_pay_rate-optionalunionint-float"></a>

Employee's annual pay amount (in dollars). Only used if Type=Salary.  * For Salary Type, AnnualPayRate overrides payRate if passed into API call. The value not provided will be calculated based on Employee's Annual Hours setup on Employee's Profile. * For Hourly Type, this parameter is ignored - Paycor calculates based on Employee's Annual Hours setup on Employee's Profile.             

##### type: [`PayType`](./paycor_python_sdk/type/pay_type.py)<a id="type-paytypepaycor_python_sdktypepay_typepy"></a>

##### reason: `Optional[str]`<a id="reason-optionalstr"></a>

Reason associated with the employee's pay rate. Optional.              

##### notes: `Optional[str]`<a id="notes-optionalstr"></a>

Notes associated with the employee's pay rate, which will be displayed on Pay Rate History page.  Must be 512 characters or less. Optional.              

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeePayRate3`](./paycor_python_sdk/type/employee_pay_rate3.py)
EmployeePayRate with ID set and fields updated

#### 🔄 Return<a id="🔄-return"></a>

[`CreateOrUpdateResponse`](./paycor_python_sdk/pydantic/create_or_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/payrates/{payrateId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_pay_schedule.get_upcoming_check_dates`<a id="paycoremployee_pay_scheduleget_upcoming_check_dates"></a>

This API will return upcoming pay scheduled for a given employee (upcoming check dates),
or allow looking up the check date for specific pay period dates.
* You must either specify the exact Period Start & End Date, or leave them blank. 
  * Alternatively you may consider 'GET Legal Entity Pay Schedule' which takes a range parameter.
  * You can look up pay period dates from 'GET Legal Entity Pay Schedule' (scheduled dates) or 'GET Legal Entity Pay Data' (actual dates)
* The actual pay dates may change depending on when the client admin processes payroll.

Data Access: View Employee Pay Schedule

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_upcoming_check_dates_response = paycor.employee_pay_schedule.get_upcoming_check_dates(
    employee_id="employeeId_example",
    period_start_date="1970-01-01T00:00:00.00Z",
    period_end_date="1970-01-01T00:00:00.00Z",
    continuation_token="string_example",
    include=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

ID of the Employee for which you want to get the Pay Schedule

##### period_start_date: `Optional[datetime]`<a id="period_start_date-optionaldatetime"></a>

Exact Period Start Date of Pay Schedule, to lookup specific payrun. 

##### period_end_date: `Optional[datetime]`<a id="period_end_date-optionaldatetime"></a>

Exact Period End Date of Pay Schedule, if you wish to filter - defaults to showing upcoming (future) runs

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get the next set of Employee Pay Schedule

##### include: List[[`Includes8`](./paycor_python_sdk/type/includes8.py)]<a id="include-listincludes8paycor_python_sdktypeincludes8py"></a>

Options to include more data: Additional Runs

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfPayPeriod`](./paycor_python_sdk/pydantic/paged_result_of_pay_period.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/payschedule` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_pay_stubs.get_by_employee_id`<a id="paycoremployee_pay_stubsget_by_employee_id"></a>

Note: Either CheckDate, ProcessDate or PlannerId is required as a parameter. You can find a list of valid dates by calling 'GET Legal Entity Pay Data by Legal Entity ID'.

Data Access: View Paystub Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_employee_id_response = paycor.employee_pay_stubs.get_by_employee_id(
    employee_id="employeeId_example",
    check_date="1970-01-01T00:00:00.00Z",
    process_date="1970-01-01T00:00:00.00Z",
    planner_id="string_example",
    include=[
        "string_example"
    ],
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

ID of an Employee for whom you want to get the Pay Stubs

##### check_date: `Optional[datetime]`<a id="check_date-optionaldatetime"></a>

Check Date of Pay Stubs - required (unless processDate supplied)

##### process_date: `Optional[datetime]`<a id="process_date-optionaldatetime"></a>

Process Date of Pay Stubs - required (unless checkDate supplied)

##### planner_id: `Optional[str]`<a id="planner_id-optionalstr"></a>

ID of the Planner for which you want to get the Pay Stubs.

##### include: List[[`Includes9`](./paycor_python_sdk/type/includes9.py)]<a id="include-listincludes9paycor_python_sdktypeincludes9py"></a>

Options to include more data: All, GrossAmount, NetAmount, Earnings, Taxes, Deductions  Data Access required  GrossAmount = View Paystub Gross Pay Information  NetAmount = View Paystub Net Pay Information  Earnings = View Paystub Earning Information  Taxes = View Paystub Tax Information  Deductions = View Paystub Deduction Information

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get the next set of Employee Pay Stubs

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfPayStub`](./paycor_python_sdk/pydantic/paged_result_of_pay_stub.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/paystubs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_pay_stubs.get_by_legal_entity`<a id="paycoremployee_pay_stubsget_by_legal_entity"></a>

Note: Either CheckDate, ProcessDate or PlannerId is required as a parameter.

Data Access: View Paystub Information by Legal Entity Id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_legal_entity_response = paycor.employee_pay_stubs.get_by_legal_entity(
    legal_entity_id=1,
    check_date="1970-01-01T00:00:00.00Z",
    process_date="1970-01-01T00:00:00.00Z",
    planner_id="string_example",
    include=[
        "string_example"
    ],
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of a Legal entity for which you want to get the Pay Stubs

##### check_date: `Optional[datetime]`<a id="check_date-optionaldatetime"></a>

Check Date of Pay Stubs - required (unless processDate supplied)

##### process_date: `Optional[datetime]`<a id="process_date-optionaldatetime"></a>

Process Date of Pay Stubs - required (unless checkDate supplied)

##### planner_id: `Optional[str]`<a id="planner_id-optionalstr"></a>

ID of the Planner for which you want to get the Pay Stubs.

##### include: List[[`Includes10`](./paycor_python_sdk/type/includes10.py)]<a id="include-listincludes10paycor_python_sdktypeincludes10py"></a>

Options to include more data: All, GrossAmount, NetAmount, Earnings, Taxes, Deductions  Data Access required  GrossAmount = View Paystub Gross Pay Information  NetAmount = View Paystub Net Pay Information  Earnings = View Paystub Earning Information  Taxes = View Paystub Tax Information  Deductions = View Paystub Deduction Information

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get the next set of Employee Pay Stubs

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfPayStub2`](./paycor_python_sdk/pydantic/paged_result_of_pay_stub2.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/paystubs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_pay_stubs.get_ytd_by_employee_id`<a id="paycoremployee_pay_stubsget_ytd_by_employee_id"></a>

* To Check Date is required parameter.  
* To get a list of check dates, you can use the GET Legal Entity Pay data endpoint.

Data Access: View Paystub Information YTD

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_ytd_by_employee_id_response = paycor.employee_pay_stubs.get_ytd_by_employee_id(
    employee_id="employeeId_example",
    to_check_date="1970-01-01T00:00:00.00Z",
    include=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

ID of an Employee for whom you want to get the Pay Stubs

##### to_check_date: `datetime`<a id="to_check_date-datetime"></a>

Check Date of latest Pay Stub for YTD data. 

##### include: List[[`Includes11`](./paycor_python_sdk/type/includes11.py)]<a id="include-listincludes11paycor_python_sdktypeincludes11py"></a>

Options to include more data: All, Earnings, Taxes, Deductions  Data Access required  Earnings = View Paystub Earning Information YTD  Taxes = View Paystub Tax Information YTD  Deductions = View Paystub Deduction Information YTD

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeePayStubHistory`](./paycor_python_sdk/pydantic/employee_pay_stub_history.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/paystubsytd` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_pay_stubs.get_ytd_by_legal_entity`<a id="paycoremployee_pay_stubsget_ytd_by_legal_entity"></a>

* To Check Date is required parameter.  
* To get a list of check dates, you can use the GET Legal Entity Pay data endpoint.

Data Access: View Paystub Information YTD By Legal Entity

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_ytd_by_legal_entity_response = paycor.employee_pay_stubs.get_ytd_by_legal_entity(
    legal_entity_id=1,
    to_check_date="1970-01-01T00:00:00.00Z",
    include=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of a Legal entity for which you want to get the Pay Stubs

##### to_check_date: `datetime`<a id="to_check_date-datetime"></a>

Check Date of latest Pay Stub for YTD data. 

##### include: List[[`Includes12`](./paycor_python_sdk/type/includes12.py)]<a id="include-listincludes12paycor_python_sdktypeincludes12py"></a>

Options to include more data: All, Earnings, Taxes, Deductions  Data Access required  Earnings = View Paystub Earning Information YTD By Legal Entity  Taxes = View Paystub Tax Information YTD By Legal Entity  Deductions = View Paystub Deduction Information YTD By Legal Entity

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfEmployeePayStubHistory`](./paycor_python_sdk/pydantic/paged_result_of_employee_pay_stub_history.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/paystubsytd` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_payroll_hours.add_hours_and_earnings_to_paygrid`<a id="paycoremployee_payroll_hoursadd_hours_and_earnings_to_paygrid"></a>

Required parameters in body are: IntegrationVendor, ProcessId, LegalEntityId, EmployeeNumber, DepartmentCode, EarningCode, BusinessStartDate

Data Access: Import Employee Hours and Earnings to Paygrid

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_hours_and_earnings_to_paygrid_response = paycor.employee_payroll_hours.add_hours_and_earnings_to_paygrid(
    integration_vendor="a",
    process_id="b962666d-8c1e-46db-a750-53edfe25d47e",
    import_employees=[
        {
            "employee_number": 33420,
            "import_earnings": [
                {
                    "department_code": 334,
                    "earning_code": "ERC300",
                    "earning_hours": 3.5,
                    "earning_amount": 150.57,
                    "earning_rate": 15.09,
                    "business_start_date": "2020-11-17T12:00:00.000Z",
                    "business_end_date": "2020-11-22T12:00:00.000Z",
                    "date_worked": "2022-01-22T12:00:00.000Z",
                    "pay_group_id": "71c9338a-4c28-0000-0000-0000712f0300",
                }
            ],
        }
    ],
    legal_entity_id=1,
    replace_data=True,
    append_data=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### integration_vendor: `str`<a id="integration_vendor-str"></a>

Required freeform field for tracking purposes. You can input your company or application name.

##### process_id: `str`<a id="process_id-str"></a>

Unique identifier of the transaction to prevent double-posting in Paycor's systems.  Please generate a new GUID (using any method) for every API call. Use the same GUID only when you want to replace existing data.

##### import_employees: List[`ImportEmployee`]<a id="import_employees-listimportemployee"></a>

List of Employees, with nested lists of Earnings, to import into Paycor's Paygrid system. 

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of the Legal Entity for which you want to set employee hours and earnings

##### replace_data: `bool`<a id="replace_data-bool"></a>

If \"True\" is passed for this query parameter and a matching ProcessID is passed, then the system will fully replace the entire record that was previously added.

##### append_data: `bool`<a id="append_data-bool"></a>

If \"True\" is passed for this query parameter, then the system will NOT replace any record that was previously added.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ImportPayrollHours`](./paycor_python_sdk/type/import_payroll_hours.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/payrollhours` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_payroll_hours.import_to_employee`<a id="paycoremployee_payroll_hoursimport_to_employee"></a>

Data Access: Import Payroll Hours to Employee

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
import_to_employee_response = paycor.employee_payroll_hours.import_to_employee(
    integration_vendor="a",
    process_id="b962666d-8c1e-46db-a750-53edfe25d47e",
    employee_number=33420,
    department_code=334,
    time_card_data=[
        {
            "earning_code": "ERC300",
            "earning_hours": 3.5,
            "business_start_date": "2020-11-17T12:00:00.000Z",
            "business_end_date": "2020-11-22T12:00:00.000Z",
        }
    ],
    employee_id="employeeId_example",
    app_id="763a5661-b518-0000-0000-000014e00100",
    legal_entity_id=100289,
    job_code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### integration_vendor: `str`<a id="integration_vendor-str"></a>

Required freeform field for tracking purposes. You can input your company or application name.

##### process_id: `str`<a id="process_id-str"></a>

Unique identifier of the transaction to prevent double-posting in Paycor's systems.  Please generate a new GUID (using any method) for every API call.

##### employee_number: `int`<a id="employee_number-int"></a>

Unique number of the employee in the tenant. Generated by Paycor. You can use any GET Employee endpoint to retrieve.

##### department_code: `int`<a id="department_code-int"></a>

Department code that the Hours should be paid under. You can use GET Legal Entity Departments to retrieve valid Code values. 

##### time_card_data: List[`TimeCardData`]<a id="time_card_data-listtimecarddata"></a>

List of the employee's earning rates, factors and amounts of type EmployeeEarningAmount.             

##### employee_id: `str`<a id="employee_id-str"></a>

ID of an Employee for whom you want to add the payroll hours

##### app_id: `Optional[str]`<a id="app_id-optionalstr"></a>

Optional field that can be used for tracking purposes. Not required for payroll processing. 

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

Unique identifier of the Legal Entity in Paycor's system.

##### job_code: `Optional[str]`<a id="job_code-optionalstr"></a>

JobCode parameter is not currently used - included for future functionality. 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeTimeCard2`](./paycor_python_sdk/type/employee_time_card2.py)
Employee Hours object

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/payrollhours` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_taxes.add_by_employee_id`<a id="paycoremployee_taxesadd_by_employee_id"></a>

* Use GET Tax Fields by Tax Code to determine payload needed to complete this call

Data Access: Create Employee Tax

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_by_employee_id_response = paycor.employee_taxes.add_by_employee_id(
    legal_entity_tax_id="b55a9eba-1007-0000-0000-000040e20100",
    reciprocity_type="LiveIn",
    withholding_effective_start_date="2020-11-13T00:00:00",
    employee_id="employeeId_example",
    filing_status="A",
    block_date="2020-11-13T00:00:00",
    non_resident_alien="true",
    is_probationary_employee=True,
    occupational_code="12",
    geographic_code="11-1011",
    soc_code="11-1012",
    seasonal_code="14",
    county_code="124",
    spouse_work="Yes/True",
    dependent_insurance_eligible="Yes/True",
    dependent_insurance_eligible_date="2020-02-13T00:00:00",
    applicable_birthyear=1980,
    adjust_withholding="N",
    amount=3141.59,
    percentage=0.2,
    ncci_code="2004",
    psd_code="101001",
    psd_rate=0.123,
    on_hold=True,
    exemptions={
        "exemptions": 3,
        "exemption_amount": 3,
        "employee_low_income_exemption": True,
        "current_year_exempt": True,
        "next_year_exempt": True,
    },
    tax_credit={
        "number_of_dependents": 8,
        "number_of_other_dependents": 0,
        "has_two_incomes": False,
        "additional_income": 123.45,
        "additional_deduction": 987.65,
        "qualified_dependent_credit": 20.2,
        "other_dependent_credit": 111.22,
        "total_credits": 123.58,
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_tax_id: `str`<a id="legal_entity_tax_id-str"></a>

Unique identifier of the legal entity tax in Paycor's system. Generated by Paycor. Retrieve a value by calling \\\"Get Legal Entity Taxes by Legal Entity ID\\\".

##### reciprocity_type: [`ReciprocityType`](./paycor_python_sdk/type/reciprocity_type.py)<a id="reciprocity_type-reciprocitytypepaycor_python_sdktypereciprocity_typepy"></a>

##### withholding_effective_start_date: `datetime`<a id="withholding_effective_start_date-datetime"></a>

Effective start date of withholding Retrieve a value by calling \\\"Get Filing Status by Tax Code\\\".

##### employee_id: `str`<a id="employee_id-str"></a>

ID of an Employee for whom you want to add the tax

##### filing_status: [`FilingStatus2`](./paycor_python_sdk/type/filing_status2.py)<a id="filing_status-filingstatus2paycor_python_sdktypefiling_status2py"></a>

##### block_date: `Optional[datetime]`<a id="block_date-optionaldatetime"></a>

Withholding block date

##### non_resident_alien: `Optional[str]`<a id="non_resident_alien-optionalstr"></a>

Specifies whether an employee is NonResidentAlien

##### is_probationary_employee: `Optional[bool]`<a id="is_probationary_employee-optionalbool"></a>

Specifies whether an employee is a probationary employee

##### occupational_code: `Optional[str]`<a id="occupational_code-optionalstr"></a>

Occupational code

##### geographic_code: `Optional[str]`<a id="geographic_code-optionalstr"></a>

Geographic code Required only for UNEAK tax

##### soc_code: `Optional[str]`<a id="soc_code-optionalstr"></a>

Standard occupational classification Code

##### seasonal_code: `Optional[str]`<a id="seasonal_code-optionalstr"></a>

Seasonal Code

##### county_code: `Optional[str]`<a id="county_code-optionalstr"></a>

County Code

##### spouse_work: `Optional[str]`<a id="spouse_work-optionalstr"></a>

Specifies  whether an employee's spouse is employed

##### dependent_insurance_eligible: `Optional[str]`<a id="dependent_insurance_eligible-optionalstr"></a>

Dependent insurance eligibility status

##### dependent_insurance_eligible_date: `Optional[datetime]`<a id="dependent_insurance_eligible_date-optionaldatetime"></a>

Dependent insurance eligibility date

##### applicable_birthyear: `Optional[int]`<a id="applicable_birthyear-optionalint"></a>

Birth year

##### adjust_withholding: [`AdjustWithholdingType`](./paycor_python_sdk/type/adjust_withholding_type.py)<a id="adjust_withholding-adjustwithholdingtypepaycor_python_sdktypeadjust_withholding_typepy"></a>

##### amount: `Optional[Union[int, float]]`<a id="amount-optionalunionint-float"></a>

Fixed, recurring deduction dollar amount.             

##### percentage: `Optional[Union[int, float]]`<a id="percentage-optionalunionint-float"></a>

Percentage value used in tax calculation. 

##### ncci_code: `Optional[str]`<a id="ncci_code-optionalstr"></a>

National Council on Compensation Insurance (NCCI) Code 

##### psd_code: `Optional[str]`<a id="psd_code-optionalstr"></a>

PA Residence PSD code- political subdivision code

##### psd_rate: `Optional[Union[int, float]]`<a id="psd_rate-optionalunionint-float"></a>

PA Residence PSD rate

##### on_hold: `Optional[bool]`<a id="on_hold-optionalbool"></a>

Whether employee tax should appear on paychecks.             

##### exemptions: [`EmployeeExemptions`](./paycor_python_sdk/type/employee_exemptions.py)<a id="exemptions-employeeexemptionspaycor_python_sdktypeemployee_exemptionspy"></a>


##### tax_credit: [`EmployeeTaxCredit`](./paycor_python_sdk/type/employee_tax_credit.py)<a id="tax_credit-employeetaxcreditpaycor_python_sdktypeemployee_tax_creditpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeTax2`](./paycor_python_sdk/type/employee_tax2.py)
EmployeeTax object

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeTaxesAddByEmployeeIdResponse`](./paycor_python_sdk/pydantic/employee_taxes_add_by_employee_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/taxes` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_taxes.get_by_employee_id`<a id="paycoremployee_taxesget_by_employee_id"></a>

Data Access: View Employee Taxes

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_employee_id_response = paycor.employee_taxes.get_by_employee_id(
    employee_id="employeeId_example",
    include=[
        "string_example"
    ],
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

ID of the employee for whom you want to get the taxes

##### include: List[[`Includes16`](./paycor_python_sdk/type/includes16.py)]<a id="include-listincludes16paycor_python_sdktypeincludes16py"></a>

Options to include more data: All, TaxCredits  Data Access required  TaxCredits = View Employee Tax Credits

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get the next set of employee taxes

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeTaxesGetByEmployeeIdResponse`](./paycor_python_sdk/pydantic/employee_taxes_get_by_employee_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/taxes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_taxes.get_filing_status_by_tax_code`<a id="paycoremployee_taxesget_filing_status_by_tax_code"></a>

Data Access: View Filing Status by Tax Code

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_filing_status_by_tax_code_response = paycor.employee_taxes.get_filing_status_by_tax_code(
    tax_code="taxCode_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tax_code: `Optional[str]`<a id="tax_code-optionalstr"></a>

You can retrieve a valid Tax Code via Get Legal Entity Taxes by Legal Entity ID

#### 🔄 Return<a id="🔄-return"></a>

[`FilingStatus`](./paycor_python_sdk/pydantic/filing_status.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/taxes/filingStatus/{taxCode}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_taxes.get_tax_fields_by_tax_code`<a id="paycoremployee_taxesget_tax_fields_by_tax_code"></a>

* This endpoint will allow you to pass in a Tax Code and will return the fields that are expected to be passed for PUT/POST Employee Taxes
* To get the Tax Codes available for your account to be used for this endpoint, use GET Legal Entity Taxes by Legal Entity ID

Data Access: Get Tax Fields By Tax Code

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_tax_fields_by_tax_code_response = paycor.employee_taxes.get_tax_fields_by_tax_code(
    tax_code="taxCode_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tax_code: `Optional[str]`<a id="tax_code-optionalstr"></a>

You can retrieve a Tax fields by Tax Codes

#### 🔄 Return<a id="🔄-return"></a>

[`GlobalTaxForm`](./paycor_python_sdk/pydantic/global_tax_form.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/taxes/taxFields/{taxCode}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_taxes.update_by_employee_id`<a id="paycoremployee_taxesupdate_by_employee_id"></a>

* Use GET Tax Fields by Tax Code to determine payload needed to complete this call

Data Access: Update Employee Tax

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_employee_id_response = paycor.employee_taxes.update_by_employee_id(
    id="a5713n92-196c-0000-0000-0007d5268Sa2",
    legal_entity_tax_id="b55a9eba-1007-0000-0000-000040e20100",
    employee_id="employeeId_example",
    reciprocity_type="LiveIn",
    filing_status="A",
    withholding_effective_start_date="2020-01-13T00:00:00",
    block_date="2020-11-13T00:00:00",
    non_resident_alien="true",
    is_probationary_employee=True,
    occupational_code="12",
    geographic_code="11-1011",
    soc_code="11-1012",
    seasonal_code="14",
    county_code="124",
    spouse_work="Yes/True",
    dependent_insurance_eligible="Yes/True",
    dependent_insurance_eligible_date="2020-02-13T00:00:00",
    applicable_birthyear=1980,
    amount=3141.59,
    percentage=0.2,
    ncci_code="2004",
    psd_code="101001",
    psd_rate=0.123,
    on_hold=True,
    exemptions={
        "exemptions": 3,
        "exemption_amount": 3,
        "employee_low_income_exemption": True,
        "current_year_exempt": True,
        "next_year_exempt": True,
    },
    tax_credit={
        "number_of_dependents": 8,
        "number_of_other_dependents": 0,
        "has_two_incomes": False,
        "additional_income": 123.45,
        "additional_deduction": 987.65,
        "qualified_dependent_credit": 20.2,
        "other_dependent_credit": 111.22,
        "total_credits": 123.58,
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Unique identifier of the employee tax in Paycor's system. Generated by Paycor.

##### legal_entity_tax_id: `str`<a id="legal_entity_tax_id-str"></a>

Unique identifier of the legal entity tax in Paycor's system. Generated by Paycor.

##### employee_id: `str`<a id="employee_id-str"></a>

ID of an Employee for whom you want to update the tax

##### reciprocity_type: [`ReciprocityType`](./paycor_python_sdk/type/reciprocity_type.py)<a id="reciprocity_type-reciprocitytypepaycor_python_sdktypereciprocity_typepy"></a>

##### filing_status: [`FilingStatus2`](./paycor_python_sdk/type/filing_status2.py)<a id="filing_status-filingstatus2paycor_python_sdktypefiling_status2py"></a>

##### withholding_effective_start_date: `Optional[datetime]`<a id="withholding_effective_start_date-optionaldatetime"></a>

Effective start date of withholding

##### block_date: `Optional[datetime]`<a id="block_date-optionaldatetime"></a>

Withholding block date

##### non_resident_alien: `Optional[str]`<a id="non_resident_alien-optionalstr"></a>

Specifies whether an employee is NonResidentAlien

##### is_probationary_employee: `Optional[bool]`<a id="is_probationary_employee-optionalbool"></a>

Specifies whether an employee is a probationary employee

##### occupational_code: `Optional[str]`<a id="occupational_code-optionalstr"></a>

Occupational code

##### geographic_code: `Optional[str]`<a id="geographic_code-optionalstr"></a>

Geographic code Required only for UNEAK tax

##### soc_code: `Optional[str]`<a id="soc_code-optionalstr"></a>

Standard occupational classification Code

##### seasonal_code: `Optional[str]`<a id="seasonal_code-optionalstr"></a>

Seasonal Code 

##### county_code: `Optional[str]`<a id="county_code-optionalstr"></a>

County Code

##### spouse_work: `Optional[str]`<a id="spouse_work-optionalstr"></a>

Specifies  whether an employee's spouse is employed

##### dependent_insurance_eligible: `Optional[str]`<a id="dependent_insurance_eligible-optionalstr"></a>

Dependent insurance eligibility status

##### dependent_insurance_eligible_date: `Optional[datetime]`<a id="dependent_insurance_eligible_date-optionaldatetime"></a>

Dependent insurance eligibility date

##### applicable_birthyear: `Optional[int]`<a id="applicable_birthyear-optionalint"></a>

Birth year

##### amount: `Optional[Union[int, float]]`<a id="amount-optionalunionint-float"></a>

Fixed, recurring deduction dollar amount.             

##### percentage: `Optional[Union[int, float]]`<a id="percentage-optionalunionint-float"></a>

Percentage value used in tax calculation. 

##### ncci_code: `Optional[str]`<a id="ncci_code-optionalstr"></a>

National Council on Compensation Insurance (NCCI) Code 

##### psd_code: `Optional[str]`<a id="psd_code-optionalstr"></a>

PA Residence PSD code- political subdivision code

##### psd_rate: `Optional[Union[int, float]]`<a id="psd_rate-optionalunionint-float"></a>

PA Residence PSD rate

##### on_hold: `Optional[bool]`<a id="on_hold-optionalbool"></a>

Whether employee tax should appear on paychecks.             

##### exemptions: [`EmployeeExemptions`](./paycor_python_sdk/type/employee_exemptions.py)<a id="exemptions-employeeexemptionspaycor_python_sdktypeemployee_exemptionspy"></a>


##### tax_credit: [`EmployeeTaxCredit`](./paycor_python_sdk/type/employee_tax_credit.py)<a id="tax_credit-employeetaxcreditpaycor_python_sdktypeemployee_tax_creditpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeTax3`](./paycor_python_sdk/type/employee_tax3.py)
EmployeeTax object

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeTaxesUpdateByEmployeeIdResponse`](./paycor_python_sdk/pydantic/employee_taxes_update_by_employee_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/taxes` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_time_card_punches.get_by_employee_id`<a id="paycoremployee_time_card_punchesget_by_employee_id"></a>

This pulls Punches data from Paycor's Perform Time system for one employee.
* Clients *do not* need to run payroll before hours are returned by this endpoint.
* Our Public API currently does not include whether the hours have already been Approved or not.
* Time Card punches may be delayed by 20 minutes.

Date requirements:
* Start Date and End Date must not be more than one year ago
* Start Date must not be in future
* Start date and end date range can be no greater than 90 days

Data Access: View Employee Time Card Punches

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_employee_id_response = paycor.employee_time_card_punches.get_by_employee_id(
    employee_id="employeeId_example",
    start_date="1970-01-01T00:00:00.00Z",
    end_date="1970-01-01T00:00:00.00Z",
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

ID of employee for which you want to get hours

##### start_date: `datetime`<a id="start_date-datetime"></a>

Date range filter, showing which records to return

##### end_date: `datetime`<a id="end_date-datetime"></a>

Date range filter, showing which records to return

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get next set of Employee Time Cards. ContinuationToken would be valid only for 24 hours. If a call is made after 24 hours with old continuationToken, no data will be retrieved.

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfTimeCardV3`](./paycor_python_sdk/pydantic/paged_result_of_time_card_v3.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/punches` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_time_card_punches.get_by_legal_entity_id`<a id="paycoremployee_time_card_punchesget_by_legal_entity_id"></a>

This pulls Punches data from Paycor's Perform Time system, for one legal entity.
* Clients *do not* need to run payroll before hours are returned by this endpoint.
* Our Public API currently does not include whether the hours have already been Approved or not.
* Time Card hours may be delayed by 20 minutes.

Date requirements:
* Start Date and End Date must not be more than one year ago
* Start Date must not be in future
* Start date and end date range can be no greater than 90 days

Data Access: View Employee Time Card Punches By Legal Entity Id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_legal_entity_id_response = paycor.employee_time_card_punches.get_by_legal_entity_id(
    legal_entity_id=1,
    start_date="1970-01-01T00:00:00.00Z",
    end_date="1970-01-01T00:00:00.00Z",
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of legal entity for which you want to get hours

##### start_date: `datetime`<a id="start_date-datetime"></a>

Date range filter, showing which records to return

##### end_date: `datetime`<a id="end_date-datetime"></a>

Date range filter, showing which records to return

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get next set of Employee Time Cards. ContinuationToken would be valid only for 24 hours. If a call is made after 24 hours with old continuationToken, no data will be retrieved.

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfTimeCardV3`](./paycor_python_sdk/pydantic/paged_result_of_time_card_v3.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalEntities/{legalEntityId}/punches` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_time_off_accruals.get_by_employee_id`<a id="paycoremployee_time_off_accrualsget_by_employee_id"></a>

Data Access: View Employee Timeoff Accruals by Employee Id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_employee_id_response = paycor.employee_time_off_accruals.get_by_employee_id(
    employee_id="employeeId_example",
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

ID of an Employee for whom you want to get the Balances

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get the next set of Employee Balances

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfEmployeeBalance`](./paycor_python_sdk/pydantic/paged_result_of_employee_balance.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/timeoffaccruals` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employee_time_off_accruals.get_by_legal_entity_id`<a id="paycoremployee_time_off_accrualsget_by_legal_entity_id"></a>

Data Access: View Employee Timeoff Accruals by Legal Entity Id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_legal_entity_id_response = paycor.employee_time_off_accruals.get_by_legal_entity_id(
    legal_entity_id=1,
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

Legal entity ID for which you want to get the balances

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get the next set of employee balances

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfEmployeeBalance`](./paycor_python_sdk/pydantic/paged_result_of_employee_balance.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/timeoffaccruals` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employees.create_new_employee`<a id="paycoremployeescreate_new_employee"></a>

This immediately "hires" a new employee and associated Person in Paycor's system. There is no way to undo or reverse this operation.
After creating an employee, please wait sixty seconds before using employeeId to call other endpoints.
            
Data Access: Create Employee

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_employee_response = paycor.employees.create_new_employee(
    legal_entity_id=123666,
    first_name="Charles",
    last_name="Dodgson",
    hire_date="2000-11-01T00:00:00Z",
    status="Active",
    paygroup_description="a",
    department_code=1,
    primary_address={
        "street_line1": "4811 Montgomery Road",
        "street_line2": "Building A",
        "suite": "Suite 100",
        "city": "Cincinnati",
        "state": "OH",
        "country": "USA",
        "county": "Hamilton",
        "zip_code": "45212",
    },
    employee_number=12345,
    alternate_employee_number="1234567890",
    prefix="None",
    middle_name="Lutwidge",
    suffix="None",
    home_email="string_example",
    work_email="string_example",
    phones=[
        {
            "country_code": "+1",
            "area_code": "513",
            "phone_number": "555-2300",
            "type": "Unknown",
        }
    ],
    social_security_number="555555555",
    birth_date="1944-04-01T00:00:00Z",
    gender="Male",
    ethnicity="AmerIndorAKNative",
    marital_status="Single",
    work_location="string_example",
    job_title="Software Engineer",
    re_hire_date="2020-05-21T00:00:00Z",
    flsa="HourlyExempt",
    type="Casual",
    manager_emp_id="52a2s23-0000-0000-0000-0007d0009840",
    veteran="true",
    disability="true",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

Employee's LegalEntityId.             

##### first_name: `str`<a id="first_name-str"></a>

First name of the employee.

##### last_name: `str`<a id="last_name-str"></a>

Last name of the employee.

##### hire_date: `datetime`<a id="hire_date-datetime"></a>

Date the employee was hired following the ISO 8601 standard.. Format: YYYY-MM-DDTHH:MM:SSZ  (ISO-8601 standard)              

##### status: [`EmploymentStatus`](./paycor_python_sdk/type/employment_status.py)<a id="status-employmentstatuspaycor_python_sdktypeemployment_statuspy"></a>

##### paygroup_description: `str`<a id="paygroup_description-str"></a>

The description of the paygroup that the employee belongs to.  * Must be existing Paygroup. Call GET Pay Groups by LegalEntityID to lookup valid values in the field \\\"PaygroupName\\\".              

##### department_code: `int`<a id="department_code-int"></a>

The department code that the employee belongs to.   * Must be existing Department. Call Get Legal Entity Departments by LegalEntityID to get valid Code value.             

##### primary_address: [`GenericAddress`](./paycor_python_sdk/type/generic_address.py)<a id="primary_address-genericaddresspaycor_python_sdktypegeneric_addresspy"></a>


##### employee_number: `Optional[int]`<a id="employee_number-optionalint"></a>

Unique number of the employee in the tenant. Generated by Paycor if not provided.             

##### alternate_employee_number: `Optional[str]`<a id="alternate_employee_number-optionalstr"></a>

Can be up to 9 characters, Requires Alternate Employee Number product offering.

##### prefix: [`Prefix`](./paycor_python_sdk/type/prefix.py)<a id="prefix-prefixpaycor_python_sdktypeprefixpy"></a>

##### middle_name: `Optional[str]`<a id="middle_name-optionalstr"></a>

Middle name of the employee.

##### suffix: [`Suffix`](./paycor_python_sdk/type/suffix.py)<a id="suffix-suffixpaycor_python_sdktypesuffixpy"></a>

##### home_email: `Optional[str]`<a id="home_email-optionalstr"></a>

Home Email Information of an employee.             

##### work_email: `Optional[str]`<a id="work_email-optionalstr"></a>

Work Email Information of an employee.             

##### phones: List[`Phone`]<a id="phones-listphone"></a>

List of type Phone containing phone numbers of the employee. Accepts home,mobile and work phone numbers, upto 1 of each type. Mobile phone is accepted only if home contact is provided.              

##### social_security_number: `Optional[str]`<a id="social_security_number-optionalstr"></a>

Social security number of the employee.

##### birth_date: `Optional[datetime]`<a id="birth_date-optionaldatetime"></a>

Date of birth of the employee following the ISO 8601 standard. Format: YYYY-MM-DDTHH:MM:SSZ  (ISO-8601 standard) 

##### gender: [`Gender`](./paycor_python_sdk/type/gender.py)<a id="gender-genderpaycor_python_sdktypegenderpy"></a>

##### ethnicity: [`EthnicityType`](./paycor_python_sdk/type/ethnicity_type.py)<a id="ethnicity-ethnicitytypepaycor_python_sdktypeethnicity_typepy"></a>

##### marital_status: [`MaritalStatus`](./paycor_python_sdk/type/marital_status.py)<a id="marital_status-maritalstatuspaycor_python_sdktypemarital_statuspy"></a>

##### work_location: `Optional[str]`<a id="work_location-optionalstr"></a>

The name of the Work Location to associate with new hire.  * Must be an existing Work Location. Use API 'GET Legal Entity Work Location by Legal Entity ID' to retrieve a list of valid names.             

##### job_title: `Optional[str]`<a id="job_title-optionalstr"></a>

Name of the Job Title to associate with new hire.  * Must be an existing Job setup on the Tenant. Use API 'GET Tenant Job Titles by TenantId' to retrieve a list of valid names.             

##### re_hire_date: `Optional[datetime]`<a id="re_hire_date-optionaldatetime"></a>

Re-hire date of the employee. Terminated employees can be rehired.  Format: YYYY-MM-DDTHH:MM:SSZ  (ISO-8601 standard) 

##### flsa: [`FlsaType`](./paycor_python_sdk/type/flsa_type.py)<a id="flsa-flsatypepaycor_python_sdktypeflsa_typepy"></a>

##### type: [`EmploymentType`](./paycor_python_sdk/type/employment_type.py)<a id="type-employmenttypepaycor_python_sdktypeemployment_typepy"></a>

##### manager_emp_id: `Optional[str]`<a id="manager_emp_id-optionalstr"></a>

Unique identifier of the manager in Paycor's system. Generated by Paycor.

##### veteran: [`VeteranStatus`](./paycor_python_sdk/type/veteran_status.py)<a id="veteran-veteranstatuspaycor_python_sdktypeveteran_statuspy"></a>

##### disability: [`DisabilityStatus`](./paycor_python_sdk/type/disability_status.py)<a id="disability-disabilitystatuspaycor_python_sdktypedisability_statuspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Employee2`](./paycor_python_sdk/type/employee2.py)
Create Employee model

#### 🔄 Return<a id="🔄-return"></a>

[`CreateOrUpdateResponse`](./paycor_python_sdk/pydantic/create_or_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employees.get_by_employee_id`<a id="paycoremployeesget_by_employee_id"></a>

Tip: you can retrieve a valid EmployeeID guid via endpoints like 'Get Employees by Legal Entity ID'
            
Data Access: View Employee Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_employee_id_response = paycor.employees.get_by_employee_id(
    employee_id="employeeId_example",
    include=[
        "string_example"
    ],
    email_type="Work",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

ID of the Employee you want to get

##### include: List[[`Includes13`](./paycor_python_sdk/type/includes13.py)]<a id="include-listincludes13paycor_python_sdktypeincludes13py"></a>

Options to include more data: All, EmploymentDates, Status, Position, WorkLocation              Data Access required              EmploymentDates = View Employee Employment Dates              Status = View Employee Status              Position = View Employee Position              WorkLocation = View Employee Work Location

##### email_type: [`EmailTypeOptions`](./paycor_python_sdk/type/.py)<a id="email_type-emailtypeoptionspaycor_python_sdktypepy"></a>

Options to specify which emaill address to return. Work email type will be returned if none are specified: Home, Work

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeReturnItem`](./paycor_python_sdk/pydantic/employee_return_item.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employees.get_identifying_data`<a id="paycoremployeesget_identifying_data"></a>

Data Access: View Legal Entity Employees Identifying Data
            
Optional Data Access: View Legal Entity Employees SSN and BirthDate

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_identifying_data_response = paycor.employees.get_identifying_data(
    legal_entity_id=1,
    include=[
        "string_example"
    ],
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of the legal entity for which you want to get employees

##### include: List[[`Includes15`](./paycor_python_sdk/type/includes15.py)]<a id="include-listincludes15paycor_python_sdktypeincludes15py"></a>

Options to filter employees by employment status: Active, Inactive

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get the next set of data

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfEmployeesIdentifyingData`](./paycor_python_sdk/pydantic/paged_result_of_employees_identifying_data.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/employeesIdentifyingData` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employees.list_by_legal_entity_id`<a id="paycoremployeeslist_by_legal_entity_id"></a>

Data Access: View Legal Entity Employees

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_by_legal_entity_id_response = paycor.employees.list_by_legal_entity_id(
    legal_entity_id=1,
    include=[
        "string_example"
    ],
    email_type="Work",
    status_filter="Active",
    employee_number=1,
    last_name="string_example",
    department_code=1,
    work_location_name="string_example",
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of the legal entity for which you want to get employees

##### include: List[[`Includes14`](./paycor_python_sdk/type/includes14.py)]<a id="include-listincludes14paycor_python_sdktypeincludes14py"></a>

Options to include more data: All, EmploymentDates, Status, Position, WorkLocation              Data Access required              EmploymentDates = View Legal Entity Employees Employment Dates              Status = View Legal Entity Employees Status              Position = View Legal Entity Employees Position              WorkLocation = View Legal Entity Employees Work Location

##### email_type: [`EmailTypeOptions2`](./paycor_python_sdk/type/.py)<a id="email_type-emailtypeoptions2paycor_python_sdktypepy"></a>

Options to specify which email address to return. Work email type will be returned if none are specified: Home, Work

##### status_filter: [`EmploymentStatus`](./paycor_python_sdk/type/.py)<a id="status_filter-employmentstatuspaycor_python_sdktypepy"></a>

Option to filter by employment status.

##### employee_number: `Optional[int]`<a id="employee_number-optionalint"></a>

Option to filter by Employee Number.

##### last_name: `Optional[str]`<a id="last_name-optionalstr"></a>

Option to filter by Employee Last Name.

##### department_code: `Optional[int]`<a id="department_code-optionalint"></a>

Option to filter by Department Code.

##### work_location_name: `Optional[str]`<a id="work_location_name-optionalstr"></a>

Option to filter by Work Location Name.

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get the next set of employees

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfEmployeeReturnItem`](./paycor_python_sdk/pydantic/paged_result_of_employee_return_item.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/employees` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employees.list_by_tenant_id`<a id="paycoremployeeslist_by_tenant_id"></a>

Data Access: View Tenant Employees

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_by_tenant_id_response = paycor.employees.list_by_tenant_id(
    tenant_id=1,
    status_filter="Active",
    employee_number=1,
    last_name="string_example",
    department_code=1,
    work_location_name="string_example",
    job_code="string_example",
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_id: `int`<a id="tenant_id-int"></a>

ID of the tenant for which you want to get employees

##### status_filter: [`EmploymentStatus`](./paycor_python_sdk/type/.py)<a id="status_filter-employmentstatuspaycor_python_sdktypepy"></a>

Option to filter by employment status

##### employee_number: `Optional[int]`<a id="employee_number-optionalint"></a>

Option to filter by Employee Number.

##### last_name: `Optional[str]`<a id="last_name-optionalstr"></a>

Option to filter by Employee Last Name.

##### department_code: `Optional[int]`<a id="department_code-optionalint"></a>

Option to filter by Department Code.

##### work_location_name: `Optional[str]`<a id="work_location_name-optionalstr"></a>

Option to filter by Work Location Name.

##### job_code: `Optional[str]`<a id="job_code-optionalstr"></a>

Option to filter by Job Code.

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get the next set of employees

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfEmployeeList`](./paycor_python_sdk/pydantic/paged_result_of_employee_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/tenants/{tenantId}/employees` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employees.update_contact`<a id="paycoremployeesupdate_contact"></a>

This immediately updates an employee's contact information and associated Person's in Paycor's system.
            
Data Access: Update Employee Contact

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_contact_response = paycor.employees.update_contact(
    employee_id="employeeId_example",
    home_email="string_example",
    work_email="string_example",
    phones=[
        {
            "country_code": "+1",
            "area_code": "513",
            "phone_number": "555-2300",
            "type": "Unknown",
        }
    ],
    primary_address={
        "street_line1": "4811 Montgomery Road",
        "street_line2": "Building A",
        "suite": "Suite 100",
        "city": "Cincinnati",
        "state": "OH",
        "country": "USA",
        "county": "Hamilton",
        "zip_code": "45212",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

Id of the employee

##### home_email: `Optional[str]`<a id="home_email-optionalstr"></a>

Home Email Address of an employee.             

##### work_email: `Optional[str]`<a id="work_email-optionalstr"></a>

Work Email Address of an employee.             

##### phones: List[`Phone`]<a id="phones-listphone"></a>

List of type Phone containing phone numbers of the employee. Accepts Home, Mobile and Work phone numbers, upto 1 of each type. Only the specific number types passed in will be updated, existing phone numbers will remain unchanged.             

##### primary_address: [`GenericAddress`](./paycor_python_sdk/type/generic_address.py)<a id="primary_address-genericaddresspaycor_python_sdktypegeneric_addresspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeContact`](./paycor_python_sdk/type/employee_contact.py)
Put Employee Contact model

#### 🔄 Return<a id="🔄-return"></a>

[`CreateOrUpdateResponse`](./paycor_python_sdk/pydantic/create_or_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employees.update_paygroup`<a id="paycoremployeesupdate_paygroup"></a>

This endpoint updates an employee's paygroup.
            
Data Access: Update Employee Paygroup

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_paygroup_response = paycor.employees.update_paygroup(
    employee_id="employeeId_example",
    pay_group_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

Id of the employee

##### pay_group_id: `str`<a id="pay_group_id-str"></a>

ID of the Paygroup for whom you want to get the Pay Schedule. Available via 'GET Legal Entity Pay Groups'

#### 🔄 Return<a id="🔄-return"></a>

[`CreateOrUpdateResponse`](./paycor_python_sdk/pydantic/create_or_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/Paygroup` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employees.update_personal_data`<a id="paycoremployeesupdate_personal_data"></a>

This endpoint updates an employee's personal information.
            
Data Access: Update Employee Identifying Data

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_personal_data_response = paycor.employees.update_personal_data(
    first_name="Charles",
    last_name="Peterson",
    suffix="None",
    social_security_number="555555555",
    birth_date="1944-04-01T00:00:00Z",
    employee_id="employeeId_example",
    middle_name="Hubble",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### first_name: `str`<a id="first_name-str"></a>

First name of the employee.

##### last_name: `str`<a id="last_name-str"></a>

Last name of the employee.

##### suffix: [`Suffix`](./paycor_python_sdk/type/suffix.py)<a id="suffix-suffixpaycor_python_sdktypesuffixpy"></a>

##### social_security_number: `str`<a id="social_security_number-str"></a>

Social security number of the employee.

##### birth_date: `datetime`<a id="birth_date-datetime"></a>

Date of birth of the employee. Format: YYYY-MM-DDTHH:MM:SSZ  (ISO-8601 standard) 

##### employee_id: `str`<a id="employee_id-str"></a>

Id of the employee

##### middle_name: `Optional[str]`<a id="middle_name-optionalstr"></a>

Middle name of the employee.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeIdentifyingData`](./paycor_python_sdk/type/employee_identifying_data.py)
Put Employee Identifying data model

#### 🔄 Return<a id="🔄-return"></a>

[`CreateOrUpdateResponse`](./paycor_python_sdk/pydantic/create_or_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/identifyingdata` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employees.update_position_and_status_data`<a id="paycoremployeesupdate_position_and_status_data"></a>

This endpoint updates an employee's status and position information.
            
Data Access: Update Employee Position And Status

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_position_and_status_data_response = paycor.employees.update_position_and_status_data(
    employment_status="Active",
    rehire_date="2020-05-21T00:00:00Z",
    employment_type="Casual",
    work_location="Cincinnati",
    employee_id="employeeId_example",
    job_title="Software Engineer",
    flsa="HourlyExempt",
    manager_id="44480aa9-08d8-0000-0000-0000fd0d0300",
    department_id="3c88ef90-5e35-0000-0000-0000fb0d0300",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employment_status: [`EmploymentStatus2`](./paycor_python_sdk/type/employment_status2.py)<a id="employment_status-employmentstatus2paycor_python_sdktypeemployment_status2py"></a>

##### rehire_date: `datetime`<a id="rehire_date-datetime"></a>

Re-hire date of the employee. Terminated employees can be rehired.  Format: YYYY-MM-DDTHH:MM:SSZ  (ISO-8601 standard) 

##### employment_type: [`EmploymentType`](./paycor_python_sdk/type/employment_type.py)<a id="employment_type-employmenttypepaycor_python_sdktypeemployment_typepy"></a>

##### work_location: `str`<a id="work_location-str"></a>

The name of the Work Location to associate with Employee.  * Must be an existing Work Location, use Legal Entity Work Locations to retrieve a list of valid names.             

##### employee_id: `str`<a id="employee_id-str"></a>

Id of the employee

##### job_title: `Optional[str]`<a id="job_title-optionalstr"></a>

Name of the Job Title to associate with Employee.  * Must be an existing Job setup on the Tenant. Use API 'GET Tenant Job Titles by TenantId' to retrieve a list of valid names.             

##### flsa: [`FlsaType`](./paycor_python_sdk/type/flsa_type.py)<a id="flsa-flsatypepaycor_python_sdktypeflsa_typepy"></a>

##### manager_id: `Optional[str]`<a id="manager_id-optionalstr"></a>

Unique identifier of Employee in Paycor's system.  * Must be an existing Employee, use the EmployeeID provided from other GET Employee endpoints 

##### department_id: `Optional[str]`<a id="department_id-optionalstr"></a>

Identifier of Department. * Use API 'GET Legal Entity Departments by Legal Entity id' to retrieve a list of valid departments.             

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeePositionAndStatus`](./paycor_python_sdk/type/employee_position_and_status.py)
Put Employee Position and Status model

#### 🔄 Return<a id="🔄-return"></a>

[`CreateOrUpdateResponse`](./paycor_python_sdk/pydantic/create_or_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/positionandstatus` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employees.update_position_data`<a id="paycoremployeesupdate_position_data"></a>

This endpoint updates an employee's position information.
            
Data Access: Update Employee Position

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_position_data_response = paycor.employees.update_position_data(
    employment_type="Casual",
    work_location="Cincinnati",
    employee_id="employeeId_example",
    job_title="Software Engineer",
    flsa="HourlyExempt",
    manager_id="44480aa9-08d8-0000-0000-0000fd0d0300",
    department_id="3c88ef90-5e35-0000-0000-0000fb0d0300",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employment_type: [`EmploymentType`](./paycor_python_sdk/type/employment_type.py)<a id="employment_type-employmenttypepaycor_python_sdktypeemployment_typepy"></a>

##### work_location: `str`<a id="work_location-str"></a>

The name of the Work Location to associate with Employee.  * Must be an existing Work Location. Use API 'GET Legal Entity Work Location by Legal Entity ID' to retrieve a list of valid names.             

##### employee_id: `str`<a id="employee_id-str"></a>

Id of the employee

##### job_title: `Optional[str]`<a id="job_title-optionalstr"></a>

Name of the Job Title to associate with Employee.  * Must be an existing Job setup on the Tenant. Use API 'GET Tenant Job Titles by TenantId' to retrieve a list of valid names.             

##### flsa: [`FlsaType`](./paycor_python_sdk/type/flsa_type.py)<a id="flsa-flsatypepaycor_python_sdktypeflsa_typepy"></a>

##### manager_id: `Optional[str]`<a id="manager_id-optionalstr"></a>

Unique identifier of Employee in Paycor's system. 

##### department_id: `Optional[str]`<a id="department_id-optionalstr"></a>

Identifier of Department.             

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeePosition`](./paycor_python_sdk/type/employee_position.py)
Put Employee Position model

#### 🔄 Return<a id="🔄-return"></a>

[`CreateOrUpdateResponse`](./paycor_python_sdk/pydantic/create_or_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/position` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.employees.update_status_data`<a id="paycoremployeesupdate_status_data"></a>

This endpoint updates an employee status information.
            
Data Access: Update Employee Status Data

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_status_data_response = paycor.employees.update_status_data(
    effective_date="2019-11-01T00:00:00Z",
    employee_status="Active",
    employee_id="employeeId_example",
    employee_status_reason_id="aaeeef19-7b65-4ace-a244-ae1e43c6a634",
    eligible_for_rehire="true",
    is_voluntary_by_employee=False,
    notes="Employee absence from work",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### effective_date: `datetime`<a id="effective_date-datetime"></a>

Date at which the employee status update takes effect. Format: YYYY-MM-DDTHH:MM:SSZ  (ISO-8601 standard)              

##### employee_status: [`EmploymentStatus`](./paycor_python_sdk/type/employment_status.py)<a id="employee_status-employmentstatuspaycor_python_sdktypeemployment_statuspy"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

Id of the employee

##### employee_status_reason_id: `Optional[str]`<a id="employee_status_reason_id-optionalstr"></a>

Unique Identifier for Employee Status Reason. All possible Status Reason Values can be found using Get Legal Entity Status Reason values endpoint.             

##### eligible_for_rehire: [`EligibleForRehire`](./paycor_python_sdk/type/eligible_for_rehire.py)<a id="eligible_for_rehire-eligibleforrehirepaycor_python_sdktypeeligible_for_rehirepy"></a>

##### is_voluntary_by_employee: `Optional[bool]`<a id="is_voluntary_by_employee-optionalbool"></a>

Determines if an employee termination is voluntary or not.  This is required when EmployeeStatus is updated to one of these values: Deceased, LaidOff, Resigned, Retired, Terminated. Otherwise optional.             

##### notes: `Optional[str]`<a id="notes-optionalstr"></a>

Notes associated with the employee's status update, which will be stored in Employee's Status History.             

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmployeeStatusUpdate`](./paycor_python_sdk/type/employee_status_update.py)
Put Employee Status model

#### 🔄 Return<a id="🔄-return"></a>

[`CreateOrUpdateResponse`](./paycor_python_sdk/pydantic/create_or_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/status` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.events.notify_event_details`<a id="paycoreventsnotify_event_details"></a>

Following body attributes are optionally required:
* ItemId is required when EventType is Employee.Modified
* LegalEntityId is required when EventType is LegalEntity.Modified

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
notify_event_details_response = paycor.events.notify_event_details(
    application_id="0f8fad5b-d9cb-469f-a165-70867728950e",
    notification_url="https://partner/v1/eventNotificationReceiver",
    notification_secret="Bearer WREXIDWmfhlc19eLE1vXQ5KDnGEk22AeEvGcON2L2As8I1GwDUGstl-SUfyV6V3e23v3_EVABGx",
    event_type="Employee.Modified",
    tenant_id=2080,
    item_id="89610735-e570-0000-0000-000066000000",
    legal_entity_id=501123,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### application_id: `str`<a id="application_id-str"></a>

Unique Identifier of the Application that needs mock events.             

##### notification_url: `str`<a id="notification_url-str"></a>

URL where the Event Notification has to be sent.             

##### notification_secret: `str`<a id="notification_secret-str"></a>

Secret or Security Token required to authenticate above server.             

##### event_type: `str`<a id="event_type-str"></a>

Type of Event that needs to be triggered by Paycor's System.

##### tenant_id: `int`<a id="tenant_id-int"></a>

Unique Identifier of the Tenant in Paycor's system.

##### item_id: `Optional[str]`<a id="item_id-optionalstr"></a>

Unique Identifier of the Resource change for the Event that is triggered by Paycor.             

##### legal_entity_id: `Optional[int]`<a id="legal_entity_id-optionalint"></a>

Unique Identifier of the Legal Entity in Paycor's system.             

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Command`](./paycor_python_sdk/type/command.py)
Mock Event that user wants to trigger.

#### 🔄 Return<a id="🔄-return"></a>

[`Event`](./paycor_python_sdk/pydantic/event.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/events/mockevent` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.general_ledger.get_by_legal_entity_id`<a id="paycorgeneral_ledgerget_by_legal_entity_id"></a>

* Type of report can be Regular or Setup
    * Setup report returns only department number, company department number, account name, account number, itemize, and sort sequence all other values are set to null.
    * Regular report returns all data. 
* Planner id is required if report type is set to regular

Data Access: View General Ledger

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_legal_entity_id_response = paycor.general_ledger.get_by_legal_entity_id(
    legal_entity_id=1,
    planner_id="string_example",
    report_type="Unknown",
    include=[
        "string_example"
    ],
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of the legal entity for which you want to get the general ledger items

##### planner_id: `str`<a id="planner_id-str"></a>

ID of planner, required if report type is regular

##### report_type: [`GeneralLedgerReportType`](./paycor_python_sdk/type/.py)<a id="report_type-generalledgerreporttypepaycor_python_sdktypepy"></a>

Type of General Ledger, Regular or Setup 

##### include: List[[`Includes17`](./paycor_python_sdk/type/includes17.py)]<a id="include-listincludes17paycor_python_sdktypeincludes17py"></a>

Options to include more data: EmployeeData

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get next set of General Ledger records

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfGeneralLedger`](./paycor_python_sdk/pydantic/paged_result_of_general_ledger.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/generalledger/legalentities/{legalEntityId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.general_ledger_job_costing.get_by_legal_entity_id`<a id="paycorgeneral_ledger_job_costingget_by_legal_entity_id"></a>

Data Access: View General Ledger Job Costing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_legal_entity_id_response = paycor.general_ledger_job_costing.get_by_legal_entity_id(
    legal_entity_id=1,
    planner_id="plannerId_example",
    include=[
        "string_example"
    ],
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of the legal entity for which you want to get the job costing items.

##### planner_id: `str`<a id="planner_id-str"></a>

ID of planner.

##### include: List[[`Includes18`](./paycor_python_sdk/type/includes18.py)]<a id="include-listincludes18paycor_python_sdktypeincludes18py"></a>

Options to include more data: EmployeeData

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get next set of Job Costing records.

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfJobCosting`](./paycor_python_sdk/pydantic/paged_result_of_job_costing.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/generalledger/jobcosting/legalentities/{legalEntityId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.job_titles.list_by_tenant_id`<a id="paycorjob_titleslist_by_tenant_id"></a>

Job Titles are configured at a Tenant level, unlike most other objects which are configured at a Legal Entity level.

Data Access: View Tenant Job Titles

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_by_tenant_id_response = paycor.job_titles.list_by_tenant_id(
    tenant_id=1,
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_id: `int`<a id="tenant_id-int"></a>

ID of the Tenant you want to get Job Titles.

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get the next set of Job Titles

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfTenantJobTitle`](./paycor_python_sdk/pydantic/paged_result_of_tenant_job_title.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/tenants/{tenantId}/jobtitles` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.labor_categories.by_legal_entity_id_get`<a id="paycorlabor_categoriesby_legal_entity_id_get"></a>

To make this call you will need the Job Costing or Workforce Management Service.

Data Access: View Labor Categories by Legal Entity Id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
by_legal_entity_id_get_response = paycor.labor_categories.by_legal_entity_id_get(
    legal_entity_id=1,
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of the Legal Entity for which you want to get labor categories (also known as job categories)

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfLaborCategories`](./paycor_python_sdk/pydantic/paged_result_of_labor_categories.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/laborcategories` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.labor_codes.add_labor_code_to_legal_entity`<a id="paycorlabor_codesadd_labor_code_to_legal_entity"></a>

This immediately creates a new labor code related to a Legal Entity in Paycor's system. There is no way to undo or reverse this operation.
* Required body attributes:
    * LaborCategoryId
    * Code
    * LaborCodeName

    
To make this call you will need the Job Costing or Workforce Management Service.

Data Access: Create and Update Labor Codes

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_labor_code_to_legal_entity_response = paycor.labor_codes.add_labor_code_to_legal_entity(
    labor_category_id="12e0e1c9-e8dc-ec11-912c-0050569f27b8",
    labor_code_name="IT",
    code="code 1",
    legal_entity_id=1,
    description="labor code effective until New year",
    effective_start_date="2020-05-26",
    effective_end_date="2020-11-25",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### labor_category_id: `str`<a id="labor_category_id-str"></a>

Id of the Labor Category 

##### labor_code_name: `str`<a id="labor_code_name-str"></a>

Unique name of labor code in the labor category

##### code: `str`<a id="code-str"></a>

textual code of labor code

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of the Legal Entity for which you want to create Labor Code

##### description: `Optional[str]`<a id="description-optionalstr"></a>

Description of labor code

##### effective_start_date: `Optional[datetime]`<a id="effective_start_date-optionaldatetime"></a>

Effective start date of labor code

##### effective_end_date: `Optional[datetime]`<a id="effective_end_date-optionaldatetime"></a>

Effective end date of labor code

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LaborCode3`](./paycor_python_sdk/type/labor_code3.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CreateOrUpdateResponse`](./paycor_python_sdk/pydantic/create_or_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/laborcodes` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.labor_codes.list_by_legal_entity_id`<a id="paycorlabor_codeslist_by_legal_entity_id"></a>

Returns list of all Labor Code items. 
* Labor code is not active if effective start date is after current date or if effective end date is before current date.

To make this call you will need the Job Costing or Workforce Management Service.

Data Access: View Labor Codes by Legal Entity Id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_by_legal_entity_id_response = paycor.labor_codes.list_by_legal_entity_id(
    legal_entity_id=1,
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of the Legal Entity for which you want to get labor codes (also known as job codes)

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`LaborCode4`](./paycor_python_sdk/pydantic/labor_code4.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/laborcodes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.labor_codes.update_specified_labor_code`<a id="paycorlabor_codesupdate_specified_labor_code"></a>

This operation updates specified labor code in Paycor's system.

To make this call you will need the Job Costing or Workforce Management Service.

LaborCodeId is required.

Data Access: Create and Update Labor Codes

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_specified_labor_code_response = paycor.labor_codes.update_specified_labor_code(
    labor_code_id="12e0e1c9-e8dc-ec11-912c-0050569f27b8",
    legal_entity_id=1,
    labor_code_name="IT",
    description="labor code effective until New year",
    code="code 1",
    effective_start_date="2020-05-26",
    effective_end_date="2020-11-25",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### labor_code_id: `str`<a id="labor_code_id-str"></a>

Id of the Labor Code 

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of the Legal Entity for which you want to update Labor Code

##### labor_code_name: `Optional[str]`<a id="labor_code_name-optionalstr"></a>

Unique name of labor code in the labor category

##### description: `Optional[str]`<a id="description-optionalstr"></a>

Description of labor code

##### code: `Optional[str]`<a id="code-optionalstr"></a>

textual code of labor code

##### effective_start_date: `Optional[datetime]`<a id="effective_start_date-optionaldatetime"></a>

Effective start date of labor code

##### effective_end_date: `Optional[datetime]`<a id="effective_end_date-optionaldatetime"></a>

Effective end date of labor code

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LaborCode5`](./paycor_python_sdk/type/labor_code5.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CreateOrUpdateResponse`](./paycor_python_sdk/pydantic/create_or_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/laborcodes` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.legal_entities.get_by_id`<a id="paycorlegal_entitiesget_by_id"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = paycor.legal_entities.get_by_id(
    legal_entity_id=1,
    include=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

##### include: List[[`Includes19`](./paycor_python_sdk/type/includes19.py)]<a id="include-listincludes19paycor_python_sdktypeincludes19py"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`LegalEntity`](./paycor_python_sdk/pydantic/legal_entity.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.legal_entities.get_tenant_list`<a id="paycorlegal_entitiesget_tenant_list"></a>

Get Legal Entities/Tenants for the user logged in

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_tenant_list_response = paycor.legal_entities.get_tenant_list()
```

#### 🔄 Return<a id="🔄-return"></a>

[`UserInfo`](./paycor_python_sdk/pydantic/user_info.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/ActivatedLegalEntityTenantList` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.legal_entity_activity_types.get_by_legal_entity_id`<a id="paycorlegal_entity_activity_typesget_by_legal_entity_id"></a>

Get Legal Entity Activity Types by Legal Entity ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_legal_entity_id_response = paycor.legal_entity_activity_types.get_by_legal_entity_id(
    legal_entity_id=1,
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

Legal Entity Id for whom you want to get the Activity Types

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfActivityType`](./paycor_python_sdk/pydantic/paged_result_of_activity_type.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/activitytypes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.legal_entity_certifications.list`<a id="paycorlegal_entity_certificationslist"></a>

Tip: you can retrieve a list of certiifcates via endpoints like 'Get Certificates by Legal Entity ID'

Data Access: View Certification Information for Legal Entity

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = paycor.legal_entity_certifications.list(
    legal_entity_id=1,
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`TenantCertification`](./paycor_python_sdk/pydantic/tenant_certification.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/certifications` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.legal_entity_certifications.list_certification_organizations`<a id="paycorlegal_entity_certificationslist_certification_organizations"></a>

Data Access: View Certification Organizations for Legal Entity

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_certification_organizations_response = paycor.legal_entity_certifications.list_certification_organizations(
    legal_entity_id=1,
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of the Legal Entity for which you want to get the certification organizations

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get the next set of certification organizations

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfTenantCertificationOrganization`](./paycor_python_sdk/pydantic/paged_result_of_tenant_certification_organization.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/certificationOrganizations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.legal_entity_deductions.view_employees_data`<a id="paycorlegal_entity_deductionsview_employees_data"></a>

Data Access: View Legal Entity Employees

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
view_employees_data_response = paycor.legal_entity_deductions.view_employees_data(
    legal_entity_id=1,
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of the Legal Entity for which you want to get the deductions

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get the next set of Legal Entity Deductions

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfLegalEntityDeduction`](./paycor_python_sdk/pydantic/paged_result_of_legal_entity_deduction.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/deductions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.legal_entity_departments.create_new_department`<a id="paycorlegal_entity_departmentscreate_new_department"></a>

Creates new Department for a Legal Entity.
* the newly created Department will take at least 60 seconds to propagate through the system

Data Access: Create and Update Legal Entity Departments

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_department_response = paycor.legal_entity_departments.create_new_department(
    code="123",
    parent_id="cb4a1b67-000c-0000-0000-000066000456",
    description="Department 123",
    work_location_id="cb4a1b67-000c-0000-0000-000066000212",
    legal_entity_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

User defined department code. Only numeric characters are allowed and the limit is 14 characters.

##### parent_id: `str`<a id="parent_id-str"></a>

Id of the parent department (or payroll) under which new department will be created. When creating top level departments, payroll id should be used as parent id

##### description: `str`<a id="description-str"></a>

User defined description of the department.

##### work_location_id: `str`<a id="work_location_id-str"></a>

The ID of the Work Location to associate with new department.  * Must be an existing Work Location on the Legal Entity. Use API 'Get a list of Work Locations for a Legal Entity' to retrieve a list of valid IDs.              

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of the Legal Entity for which you want to create the Departments

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Department2`](./paycor_python_sdk/type/department2.py)
Create department model

#### 🔄 Return<a id="🔄-return"></a>

[`CreateOrUpdateResponse`](./paycor_python_sdk/pydantic/create_or_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/departments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.legal_entity_departments.get_by_id`<a id="paycorlegal_entity_departmentsget_by_id"></a>

Data Access: View Legal Entity Departments by Department Id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = paycor.legal_entity_departments.get_by_id(
    legal_entity_id=1,
    department_id="departmentId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of the Legal Entity for which you want to get the Departments

##### department_id: `str`<a id="department_id-str"></a>

ID of the Department

#### 🔄 Return<a id="🔄-return"></a>

[`Department`](./paycor_python_sdk/pydantic/department.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/departments/{departmentId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.legal_entity_departments.list_by_legal_entity_id`<a id="paycorlegal_entity_departmentslist_by_legal_entity_id"></a>

Data Access: View Legal Entity Departments Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_by_legal_entity_id_response = paycor.legal_entity_departments.list_by_legal_entity_id(
    legal_entity_id=1,
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of the Legal Entity for which you want to get the Departments

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get the next set of Legal Entity Departments

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfDepartment`](./paycor_python_sdk/pydantic/paged_result_of_department.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/departments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.legal_entity_departments.update_by_legal_entity_id`<a id="paycorlegal_entity_departmentsupdate_by_legal_entity_id"></a>

Updates existing Department for a Legal Entity.
* The update of the Department will take at least 60 seconds to propagate through the system
* When updating top level departments, payroll id should be used as parent id

Data Access: Create and Update Legal Entity Departments

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_legal_entity_id_response = paycor.legal_entity_departments.update_by_legal_entity_id(
    department_id="89b88074-4b20-0000-0000-000014e00146",
    code="123",
    parent_id="cb4a1b67-000c-0000-0000-000066000456",
    description="Department 123",
    work_location_id="cb4a1b67-000c-0000-0000-000066000212",
    legal_entity_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### department_id: `str`<a id="department_id-str"></a>

Unique Identifier of the Department in Paycor's system.             

##### code: `str`<a id="code-str"></a>

User defined department code. Only numeric characters are allowed and the limit is 14 characters.

##### parent_id: `str`<a id="parent_id-str"></a>

Id of the parent department (or payroll) under which new department will be created. When updating top level departments, payroll id should be used as parent id

##### description: `str`<a id="description-str"></a>

User defined description of the department.

##### work_location_id: `str`<a id="work_location_id-str"></a>

The ID of the Work Location to associate with new department.  * Must be an existing Work Location on the Legal Entity. Use API 'Get a list of Work Locations for a Legal Entity' to retrieve a list of valid IDs.              

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of the Legal Entity for which you want to update the Department

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Department3`](./paycor_python_sdk/type/department3.py)
Update Department model

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfDepartment`](./paycor_python_sdk/pydantic/paged_result_of_department.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/departments` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.legal_entity_earnings.get_by_legal_entity_id`<a id="paycorlegal_entity_earningsget_by_legal_entity_id"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_legal_entity_id_response = paycor.legal_entity_earnings.get_by_legal_entity_id(
    legal_entity_id=1,
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`LegalEntityEarningsGetByLegalEntityIdResponse`](./paycor_python_sdk/pydantic/legal_entity_earnings_get_by_legal_entity_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/earnings` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.legal_entity_job_titles.list_by_legal_entity_id`<a id="paycorlegal_entity_job_titleslist_by_legal_entity_id"></a>

Job Titles are configured at a Tenant level, unlike most other objects which are configured at a Legal Entity level.

Data Access: View Legal Entity Job Titles

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_by_legal_entity_id_response = paycor.legal_entity_job_titles.list_by_legal_entity_id(
    legal_entity_id=1,
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of the Legal Entity you want to get Job Titles.

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get the next set of Job Titles

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfTenantJobTitle`](./paycor_python_sdk/pydantic/paged_result_of_tenant_job_title.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/jobtitles` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.legal_entity_pay_data.get_pay_dates`<a id="paycorlegal_entity_pay_dataget_pay_dates"></a>

This endpoint returns the dates that particular employees were actually paid.
* You can retrieve all employees by not passing EmployeeId, or you can pass EmployeeId to filter.
* The returned values (Check Date or Process Date) can be used as an input for GET Employee Pay Stubs.
* Only dates from provided fromCheckDate and toCheckDate are used.
* Requires exactly one filtering parameter to be passed in. Choose *one* of these three:
  * Check Date range: parameters fromCheckDate and toCheckDate
  * Process Date: the single date the payrun was processed.
  * PlannerID: You can retrieve your Planner ID by using the Legal Entity Payroll Processing Data endpoint.
* Returns one object per pay date, even if there were multiple paychecks on that same date.
* Does include Additional Payruns, which don't have to follow the schedule and can be used for bonuses.

Data Access: View Paydata Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_pay_dates_response = paycor.legal_entity_pay_data.get_pay_dates(
    legal_entity_id=1,
    employee_id="string_example",
    from_check_date="1970-01-01T00:00:00.00Z",
    to_check_date="1970-01-01T00:00:00.00Z",
    process_date="1970-01-01T00:00:00.00Z",
    planner_id="string_example",
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of the Legal Entity for which you want to get the Pay Data

##### employee_id: `Optional[str]`<a id="employee_id-optionalstr"></a>

ID of an Employee, if you want to filter to paydata from a specific Employee

##### from_check_date: `Optional[datetime]`<a id="from_check_date-optionaldatetime"></a>

Filter Option 1: Date Range, From Check Date of Payrun

##### to_check_date: `Optional[datetime]`<a id="to_check_date-optionaldatetime"></a>

Filter Option 1: Date Range, To Check Date of Payrun

##### process_date: `Optional[datetime]`<a id="process_date-optionaldatetime"></a>

Filter Option 2: Process Date of Payrun

##### planner_id: `Optional[str]`<a id="planner_id-optionalstr"></a>

Filter Option 3: ID of the Planner for which you want to get the Pay Data.

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get the next set of Legal Entity Pay Data

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfLegalEntityPayData`](./paycor_python_sdk/pydantic/paged_result_of_legal_entity_pay_data.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/paydata` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.legal_entity_pay_groups.list_by_legal_entity_id`<a id="paycorlegal_entity_pay_groupslist_by_legal_entity_id"></a>

Data Access: View Legal Entity Pay Groups

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_by_legal_entity_id_response = paycor.legal_entity_pay_groups.list_by_legal_entity_id(
    legal_entity_id=1,
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of the Legal Entity for which you want to get the Pay Groups

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get the next set of Legal Entity Pay Groups

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfPayGroup`](./paycor_python_sdk/pydantic/paged_result_of_pay_group.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/payGroups` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.legal_entity_pay_schedule.get_by_legal_entity_and_paygroup`<a id="paycorlegal_entity_pay_scheduleget_by_legal_entity_and_paygroup"></a>

This returns the schedule of regularly-scheduled payruns for a given Paygroup and date range. 
* Tip: first list the Paygroups within a Legal Entity using GET Legal Entity Pay Groups, in order to populate the payGroupId parameter
* Tip: You can take the returned Check Dates or Process Dates and pass into Get Employee Pay Stubs by EmployeeID

Note that query parameters PayGroupId, AsOfDate and UntilDate are required.

Data Access: View Pay Schedule Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_legal_entity_and_paygroup_response = paycor.legal_entity_pay_schedule.get_by_legal_entity_and_paygroup(
    legal_entity_id=1,
    pay_group_id="string_example",
    as_of_date="1970-01-01T00:00:00.00Z",
    until_date="1970-01-01T00:00:00.00Z",
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of the Legal Entity for which you want to get the Pay Schedule

##### pay_group_id: `str`<a id="pay_group_id-str"></a>

ID of the Paygroup for whom you want to get the Pay Schedule. Available via 'GET Legal Entity Pay Groups'

##### as_of_date: `datetime`<a id="as_of_date-datetime"></a>

Acts as a 'start date' filter - looks for Payruns that are in-progress or unpaid as of this date

##### until_date: `datetime`<a id="until_date-datetime"></a>

Acts as an 'end date' filter - looks for Payruns that are in-progress or unpaid until this date

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get the next set of Legal Entity Pay Schedule

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfPayPeriod`](./paycor_python_sdk/pydantic/paged_result_of_pay_period.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/payschedule` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.legal_entity_payroll_processing_data.get_by_legal_entity`<a id="paycorlegal_entity_payroll_processing_dataget_by_legal_entity"></a>

* If fromCheckDate is not provided, current date will be used.

Data Access: View Legal Entity Payroll Processing Data

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_legal_entity_response = paycor.legal_entity_payroll_processing_data.get_by_legal_entity(
    legal_entity_id=1,
    from_check_date="1970-01-01T00:00:00.00Z",
    to_check_date="1970-01-01T00:00:00.00Z",
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of the Legal Entity for which you want to get the Pay Groups

##### from_check_date: `Optional[datetime]`<a id="from_check_date-optionaldatetime"></a>

Date range filter, From Check Date 

##### to_check_date: `Optional[datetime]`<a id="to_check_date-optionaldatetime"></a>

Date range filter, To Check Date

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get the next set of Legal Entity Payroll Processing Data

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfPayPeriod2`](./paycor_python_sdk/pydantic/paged_result_of_pay_period2.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/payrollProcessing` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.legal_entity_schedule_groups.get_by_legal_entity_id`<a id="paycorlegal_entity_schedule_groupsget_by_legal_entity_id"></a>

Data Access: View Legal Entity Schedule Groups

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_legal_entity_id_response = paycor.legal_entity_schedule_groups.get_by_legal_entity_id(
    legal_entity_id=1,
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of the Legal Entity you want to get Schedule Groups

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

A token to get next set of results

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfScheduleGroup`](./paycor_python_sdk/pydantic/paged_result_of_schedule_group.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/schedulegroups` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.legal_entity_services.get_subscribed_services`<a id="paycorlegal_entity_servicesget_subscribed_services"></a>

Data Access: View Legal Entity Services

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_subscribed_services_response = paycor.legal_entity_services.get_subscribed_services(
    legal_entity_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of the Legal Entity you want to get (synonymous to Paycor's ClientID)

#### 🔄 Return<a id="🔄-return"></a>

[`Services`](./paycor_python_sdk/pydantic/services.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/services` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.legal_entity_status_reason.get_list`<a id="paycorlegal_entity_status_reasonget_list"></a>

Data Access: Legal Entity Status Reason

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = paycor.legal_entity_status_reason.get_list(
    legal_entity_id=1,
    status_category="TerminationReason",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of the legal entity for which you want to get the status reasons items

##### status_category: [`StatusCategory2`](./paycor_python_sdk/type/.py)<a id="status_category-statuscategory2paycor_python_sdktypepy"></a>

Status category of status reasons.

#### 🔄 Return<a id="🔄-return"></a>

[`LegalEntityStatusReasonGetListResponse`](./paycor_python_sdk/pydantic/legal_entity_status_reason_get_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/statusReasons/{statusCategory}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.legal_entity_time_data.get_time_off_request_error_logs_by_tracking_id`<a id="paycorlegal_entity_time_dataget_time_off_request_error_logs_by_tracking_id"></a>

Data Access: View Timeoff Requests by Timeoff Request Id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_time_off_request_error_logs_by_tracking_id_response = paycor.legal_entity_time_data.get_time_off_request_error_logs_by_tracking_id(
    legal_entity_id=1,
    tracking_id="trackingId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of the Legal Entity for which you want to get the Timeoff Request.

##### tracking_id: `str`<a id="tracking_id-str"></a>

ID of the Employee Timeoff Request failure result.

#### 🔄 Return<a id="🔄-return"></a>

[`TimeOffRequestsErrorLog`](./paycor_python_sdk/pydantic/time_off_requests_error_log.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/timeoffRequestserrorlog/{trackingId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.legal_entity_time_off_types.view_time_off_types`<a id="paycorlegal_entity_time_off_typesview_time_off_types"></a>

Data Access: View Time Off Types

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
view_time_off_types_response = paycor.legal_entity_time_off_types.view_time_off_types(
    legal_entity_id=1,
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of an Legal Entity for which you want to get the Time Off Types

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get the next set of results

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfTimeOffType`](./paycor_python_sdk/pydantic/paged_result_of_time_off_type.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/timeofftypes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.legal_entity_work_locations.add_by_legal_entity_id`<a id="paycorlegal_entity_work_locationsadd_by_legal_entity_id"></a>

Data Access: Create Legal Entity Work Location

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_by_legal_entity_id_response = paycor.legal_entity_work_locations.add_by_legal_entity_id(
    name="Temp WL.",
    addresses=[
        {
            "type": "Physical",
            "street_line1": "5555 Test Road",
            "street_line2": "Building 1",
            "state": "OH",
            "city": "Cincinnati",
            "country": "USA",
            "zip_code": "55555",
        }
    ],
    legal_entity_id=1,
    store_id="18",
    is_fmla_eligible=True,
    phone_numbers=[
        {
            "type": "Voice",
            "phone_number": "555-2300",
        }
    ],
    address_data=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the work location.

##### addresses: List[`WorkLocationAddress`]<a id="addresses-listworklocationaddress"></a>

A list of work location's addresses.

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

##### store_id: `Optional[str]`<a id="store_id-optionalstr"></a>

Unique identifier of the work location store. StoreId is used for clients with WOTC Service only, defaults to Worklocation name if not provided.

##### is_fmla_eligible: `Optional[bool]`<a id="is_fmla_eligible-optionalbool"></a>

Flag which determines if work location is FMLA eligible (Family and Medical Leave Act).

##### phone_numbers: List[`WorkLocationPhoneNumber`]<a id="phone_numbers-listworklocationphonenumber"></a>

A list of the work location's phone numbers.             

##### address_data: `bool`<a id="address_data-bool"></a>

Use Physical Address as mailing address?

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WorkLocation`](./paycor_python_sdk/type/work_location.py)
Create Work Location model

#### 🔄 Return<a id="🔄-return"></a>

[`CreateOrUpdateResponse`](./paycor_python_sdk/pydantic/create_or_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/worklocations` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.legal_entity_work_locations.delete_by_legal_entity_and_work_location_id`<a id="paycorlegal_entity_work_locationsdelete_by_legal_entity_and_work_location_id"></a>

Data Access: Delete Legal Entity Work Location

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_by_legal_entity_and_work_location_id_response = paycor.legal_entity_work_locations.delete_by_legal_entity_and_work_location_id(
    legal_entity_id=1,
    work_location_id="workLocationId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of the Legal Entity for which you want to delete Work Location

##### work_location_id: `str`<a id="work_location_id-str"></a>

ID of the Work Location

#### 🔄 Return<a id="🔄-return"></a>

[`CreateOrUpdateResponse`](./paycor_python_sdk/pydantic/create_or_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/worklocations/{workLocationId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.legal_entity_work_locations.get_by_legal_entity_and_location`<a id="paycorlegal_entity_work_locationsget_by_legal_entity_and_location"></a>

Data Access: View Legal Entity Work Location

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_legal_entity_and_location_response = paycor.legal_entity_work_locations.get_by_legal_entity_and_location(
    legal_entity_id=1,
    work_location_id="workLocationId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of the Legal Entity for which you want to get the work location

##### work_location_id: `str`<a id="work_location_id-str"></a>

ID of the Work Location

#### 🔄 Return<a id="🔄-return"></a>

[`LegalEntityWorkLocation`](./paycor_python_sdk/pydantic/legal_entity_work_location.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/worklocations/{workLocationId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.legal_entity_work_locations.list`<a id="paycorlegal_entity_work_locationslist"></a>

Data Access: View Legal Entity Work Locations

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = paycor.legal_entity_work_locations.list(
    legal_entity_id=1,
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of the Legal Entity for which you want to get the work locations

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get the next set of work locations

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfLegalEntityWorkLocation`](./paycor_python_sdk/pydantic/paged_result_of_legal_entity_work_location.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/worklocations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.legal_entity_work_locations.update_by_legal_entity_id`<a id="paycorlegal_entity_work_locationsupdate_by_legal_entity_id"></a>

Data Access: Update Legal Entity Work Location

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_legal_entity_id_response = paycor.legal_entity_work_locations.update_by_legal_entity_id(
    id="164f5405-d32c-4612-8a11-20491516e557",
    legal_entity_id=1,
    addresses=[
        {
            "type": "Physical",
            "street_line1": "5555 Test Road",
            "street_line2": "Building 1",
            "state": "OH",
            "city": "Cincinnati",
            "country": "USA",
            "zip_code": "55555",
        }
    ],
    phone_numbers=[
        {
            "type": "Voice",
            "phone_number": "555-2300",
        }
    ],
    time_zone="12",
    is_fmla_eligible=False,
    is_default=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Unique identifier of the work location in Paycor's system. Generated by Paycor.

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of the Legal Entity for which you want to get the work locations

##### addresses: List[`WorkLocationAddressUpdate`]<a id="addresses-listworklocationaddressupdate"></a>

A list of work location's addresses.

##### phone_numbers: List[`WorkLocationPhoneNumber`]<a id="phone_numbers-listworklocationphonenumber"></a>

A list of the work location's phone numbers.             

##### time_zone: `Optional[str]`<a id="time_zone-optionalstr"></a>

Time zone.             

##### is_fmla_eligible: `Optional[bool]`<a id="is_fmla_eligible-optionalbool"></a>

Is FmlaEligible.             

##### is_default: `Optional[bool]`<a id="is_default-optionalbool"></a>

Is default             

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WorkLocation2`](./paycor_python_sdk/type/work_location2.py)
Update Work Location model

#### 🔄 Return<a id="🔄-return"></a>

[`CreateOrUpdateResponse`](./paycor_python_sdk/pydantic/create_or_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/worklocations` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.legal_entity_work_sites.get_by_legal_entity_id`<a id="paycorlegal_entity_work_sitesget_by_legal_entity_id"></a>

Data Access: View Legal Entity Work Sites

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_legal_entity_id_response = paycor.legal_entity_work_sites.get_by_legal_entity_id(
    legal_entity_id=1,
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of the Legal Entity you want to get Work Sites

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

A token to get next set of results

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfWorkSite`](./paycor_python_sdk/pydantic/paged_result_of_work_site.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/worksites` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.persons.get_by_employee_id_person`<a id="paycorpersonsget_by_employee_id_person"></a>

Data Access: View Employee Person

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_employee_id_person_response = paycor.persons.get_by_employee_id_person(
    employee_id="employeeId_example",
    include=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

EmployeeID linked to the Person you want to get

##### include: List[[`Includes21`](./paycor_python_sdk/type/includes21.py)]<a id="include-listincludes21paycor_python_sdktypeincludes21py"></a>

Options to include more data: All, Demographic, Benefit, Military, SocialMedia, Addresses, EmployeeAssignments, EmergencyContact, SocialSecurityNumber, Phones

#### 🔄 Return<a id="🔄-return"></a>

[`Person`](./paycor_python_sdk/pydantic/person.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/person` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.persons.get_by_tenant_and_person`<a id="paycorpersonsget_by_tenant_and_person"></a>

Note that PersonID and TenantID must always be passed together.

Data Access: View Person Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_tenant_and_person_response = paycor.persons.get_by_tenant_and_person(
    tenant_id=1,
    person_id="personId_example",
    include=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_id: `int`<a id="tenant_id-int"></a>

ID of the Tenant that the Person is in

##### person_id: `str`<a id="person_id-str"></a>

ID of the Person you want to get

##### include: List[[`Includes20`](./paycor_python_sdk/type/includes20.py)]<a id="include-listincludes20paycor_python_sdktypeincludes20py"></a>

Options to include more data:  All, Demographic, Benefit, Military, SocialMedia, Addresses, EmployeeAssignments, EmergencyContact, SocialSecurityNumber, Phones  Demographic = View Person Demographic Information  Benefit = View Person Disability and Tobacco Status  Military = View Person Military  SocialMedia = View Person Social Media  Addresses = View Person Addresses  EmployeeAssignments = View Employee Records  EmergencyContact = View Person Emergency Contacts  SocialSecurityNumber = View Person SSN  Phones = View Person Phone

#### 🔄 Return<a id="🔄-return"></a>

[`Person`](./paycor_python_sdk/pydantic/person.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/tenants/{tenantId}/persons/{personId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.persons.list_by_legal_entity_id`<a id="paycorpersonslist_by_legal_entity_id"></a>

Data Access: View Legal Entity Persons

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_by_legal_entity_id_response = paycor.persons.list_by_legal_entity_id(
    legal_entity_id=1,
    include=[
        "string_example"
    ],
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of the Legal Entity for which you want to get the persons

##### include: List[[`IncludesList`](./paycor_python_sdk/type/includes_list.py)]<a id="include-listincludeslistpaycor_python_sdktypeincludes_listpy"></a>

Options to include more data: All, Demographic, Benefit, Military, SocialMedia, Addresses, EmployeeAssignments, SocialSecurityNumber, Phones  Data Access required  Demographic = View Person Demographic Information  Benefit = View Person Disability and Tobacco Status  Military = View Person Military  SocialMedia = View Person Social Media  Addresses = View Person Addresses  EmployeeAssignments = View Employee Records

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get the next set of persons

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfPerson`](./paycor_python_sdk/pydantic/paged_result_of_person.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalEntities/{legalEntityId}/persons` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.persons.list_by_tenant_id`<a id="paycorpersonslist_by_tenant_id"></a>

PersonList provides a subset of the full Person fields.

Data Access: View Tenant Persons

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_by_tenant_id_response = paycor.persons.list_by_tenant_id(
    tenant_id=1,
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_id: `int`<a id="tenant_id-int"></a>

ID of the Tenant for which you want to get persons

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get the next set of persons

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfPersonList`](./paycor_python_sdk/pydantic/paged_result_of_person_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/tenants/{tenantId}/persons` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.tenants.get_by_id`<a id="paycortenantsget_by_id"></a>

Data Access: View Tenant Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = paycor.tenants.get_by_id(
    tenant_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_id: `int`<a id="tenant_id-int"></a>

ID of the Tenant you want to get

#### 🔄 Return<a id="🔄-return"></a>

[`Tenant`](./paycor_python_sdk/pydantic/tenant.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/tenants/{tenantId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.tenants.get_work_locations_by_tenant_id`<a id="paycortenantsget_work_locations_by_tenant_id"></a>

Work Locations are configured at a Tenant level, unlike most other objects which are configured at a Legal Entity level. 

Data Access: View Tenant Work Locations

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_work_locations_by_tenant_id_response = paycor.tenants.get_work_locations_by_tenant_id(
    tenant_id=1,
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_id: `int`<a id="tenant_id-int"></a>

ID of the Tenant you want to get work locations.

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get the next set of work locations

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfTenantWorkLocation`](./paycor_python_sdk/pydantic/paged_result_of_tenant_work_location.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/tenants/{tenantId}/worklocations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.time_off_requests.get_timeoff_request_by_id`<a id="paycortime_off_requestsget_timeoff_request_by_id"></a>

Data Access: View Timeoff Requests by Timeoff Request Id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_timeoff_request_by_id_response = paycor.time_off_requests.get_timeoff_request_by_id(
    legal_entity_id=1,
    timeoff_request_id="timeoffRequestId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of the Legal Entity for which you want to get the Timeoff Request.

##### timeoff_request_id: `str`<a id="timeoff_request_id-str"></a>

ID of the Employee Timeoff Request.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeTimeOffRequest`](./paycor_python_sdk/pydantic/employee_time_off_request.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/timeoffRequests/{timeoffRequestId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.time_off_requests.list_by_employee_id`<a id="paycortime_off_requestslist_by_employee_id"></a>

Date requirements:
* Start Date and End Date must not be more than one year ago
* Start date and end date range can be no greater than 90 days

Data Access: View Timeoff Requests by Employee Id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_by_employee_id_response = paycor.time_off_requests.list_by_employee_id(
    employee_id="employeeId_example",
    start_date="1970-01-01T00:00:00.00Z",
    end_date="1970-01-01T00:00:00.00Z",
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

ID of the Employee for which you want to get the Time Off Requests.

##### start_date: `datetime`<a id="start_date-datetime"></a>

Date range filter, showing which records to return.

##### end_date: `datetime`<a id="end_date-datetime"></a>

Date range filter, showing which records to return.

##### continuation_token: `str`<a id="continuation_token-str"></a>

Token to get the next set of results.

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfEmployeeTimeOffRequest`](./paycor_python_sdk/pydantic/paged_result_of_employee_time_off_request.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employees/{employeeId}/timeoffrequests` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paycor.time_off_requests.list_by_legal_entity_id`<a id="paycortime_off_requestslist_by_legal_entity_id"></a>

Date requirements:
* Start Date and End Date must not be more than one year ago
* Start date and end date range can be no greater than 90 days

Data Access: View Timeoff Requests by Legal Entity Id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_by_legal_entity_id_response = paycor.time_off_requests.list_by_legal_entity_id(
    legal_entity_id=1,
    start_date="1970-01-01T00:00:00.00Z",
    end_date="1970-01-01T00:00:00.00Z",
    continuation_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

ID of the Legal Entity for which you want to get the Time Off Requests.

##### start_date: `datetime`<a id="start_date-datetime"></a>

Date range filter, showing which records to return.

##### end_date: `datetime`<a id="end_date-datetime"></a>

Date range filter, showing which records to return.

##### continuation_token: `Optional[str]`<a id="continuation_token-optionalstr"></a>

Token to get the next set of results.

#### 🔄 Return<a id="🔄-return"></a>

[`PagedResultOfEmployeeTimeOffRequest`](./paycor_python_sdk/pydantic/paged_result_of_employee_time_off_request.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/legalentities/{legalEntityId}/timeoffrequests` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
