# coding: utf-8

"""
    Paycor Public API

     Welcome to Paycor's Public API! This document is a reference for the APIs Paycor has available, and acts as a complement to the \"Guides\" section.   # Getting Started  <strong>To learn more about getting started with Paycor's Public APIs, check out our <a href=\"/guides\">Guides.</a></strong>  # GET, PUT, POST  * When requesting object, use GET endpoints. All list endpoints support paging, as described [in the other doc].  * When creating an object, use POST endpoints. Your code will need to create an object and send it to Paycor in your API call request body as JSON. You can use the \"request sample\" body as a starting point. Our endpoints will return a reference to the created object (the ID and GET API URL) for your system. * When updating an object, you will use PUT endpoints. The general flow would be to: GET the object you want to update, modify the fields as desired, then PUT the object (as JSON in the request body) to our endpoints. Some fields like the object's ID cannot be updated because they are system-set.'   # Error Handling  * 400: Please consult the response text to correct your request information.  * 401 with response \"Access denied due to missing subscription key\": Please include your APIM Subscription Key as header Ocp-Apim-Subscription-Key or querystring parameter subscription-key.  * 401 with no response: Please ensure you included a valid & current Access Token in the Authorization header. * 403: Please ensure your Access Token's scope has all the relevant access you need, on the AppCreator Data Access screen.  * 404: Please validate the API route you are using. If that is correct, one of your IDs most likely does not exist or is not in a valid state.  * 429: Paycor implements rate limits for our Public API. Each customer (implemented via APIM subscription key) has a limited number of calls. The number of calls is counted across all APIs, not per individual API. Please use bulk endpoints where available and spread your calls over a wider timespan.   * The default rate limit is up to 1000 API calls per minute (total across all our Public APIs).  * 500: Please contact Paycor. When you make a POST or PUT call and receive a 500, please do not retry the call automatically - this may result in double-posting. GETs can be safely retried.   # IDs  * ClientId = LegalEntityId * TenantId = CompanyId * EmployeeId is not visible in Paycor's UI, you must retrieve it from the Public API  # Earnings, Deductions, Taxes  This section describes the domain model for Paycor's Earnings, Deductions, and Taxes. This will provide background for many paydata-related Public API endpoints.   Paycor stores Earnings, Deductions, and Taxes each at three levels: * Global: Same data across all legal entities. Setup by Paycor for customers to choose from. Sample Codes (note these will not be setup on every Legal Entity):   * Earnings: REG, OT   * Taxes: FITWH, SOC, SOCER, OHCIN   * Deductions: 401k, KMat, H125, UWay * Legal Entity or Tenant: Codes setup &amp; customized on the legal entity or Tenant level. Must be tied to a Global Code.    * Perform UI allows creating Deduction and Earning codes on Tenant level (under Configure Company nav menu). These will be returned by the Legal Entity Public API endpoints.  * Employee: codes setup on a particular employee, tied to a Legal Entity-level or Tenant-level code   * Employee Earnings/Deductions/Taxes are applied during payroll. Many properties are inherited from the Legal Entity or Global levels, but some can be overridden.   # Authentication  <!-- ReDoc-Inject: <security-definitions> -->

    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from paycor_python_sdk.pydantic.disability_status import DisabilityStatus
from paycor_python_sdk.pydantic.employment_status import EmploymentStatus
from paycor_python_sdk.pydantic.employment_type import EmploymentType
from paycor_python_sdk.pydantic.ethnicity_type import EthnicityType
from paycor_python_sdk.pydantic.flsa_type import FlsaType
from paycor_python_sdk.pydantic.gender import Gender
from paycor_python_sdk.pydantic.generic_address import GenericAddress
from paycor_python_sdk.pydantic.marital_status import MaritalStatus
from paycor_python_sdk.pydantic.phone import Phone
from paycor_python_sdk.pydantic.prefix import Prefix
from paycor_python_sdk.pydantic.suffix import Suffix
from paycor_python_sdk.pydantic.veteran_status import VeteranStatus

class Employee2(BaseModel):
    # Employee's LegalEntityId.             
    legal_entity_id: int = Field(alias='LegalEntityId')

    # First name of the employee.
    first_name: str = Field(alias='FirstName')

    # Last name of the employee.
    last_name: str = Field(alias='LastName')

    # Date the employee was hired following the ISO 8601 standard.. Format: YYYY-MM-DDTHH:MM:SSZ  (ISO-8601 standard)              
    hire_date: datetime = Field(alias='HireDate')

    status: EmploymentStatus = Field(alias='Status')

    # The description of the paygroup that the employee belongs to.  * Must be existing Paygroup. Call GET Pay Groups by LegalEntityID to lookup valid values in the field \"PaygroupName\".              
    paygroup_description: str = Field(alias='PaygroupDescription')

    # The department code that the employee belongs to.   * Must be existing Department. Call Get Legal Entity Departments by LegalEntityID to get valid Code value.             
    department_code: int = Field(alias='DepartmentCode')

    primary_address: GenericAddress = Field(alias='PrimaryAddress')

    # Unique number of the employee in the tenant. Generated by Paycor if not provided.             
    employee_number: typing.Optional[typing.Optional[int]] = Field(None, alias='EmployeeNumber')

    # Can be up to 9 characters, Requires Alternate Employee Number product offering.
    alternate_employee_number: typing.Optional[typing.Optional[str]] = Field(None, alias='AlternateEmployeeNumber')

    prefix: typing.Optional[Prefix] = Field(None, alias='Prefix')

    # Middle name of the employee.
    middle_name: typing.Optional[typing.Optional[str]] = Field(None, alias='MiddleName')

    suffix: typing.Optional[Suffix] = Field(None, alias='Suffix')

    # Home Email Information of an employee.             
    home_email: typing.Optional[typing.Optional[str]] = Field(None, alias='HomeEmail')

    # Work Email Information of an employee.             
    work_email: typing.Optional[typing.Optional[str]] = Field(None, alias='WorkEmail')

    # List of type Phone containing phone numbers of the employee. Accepts home,mobile and work phone numbers, upto 1 of each type. Mobile phone is accepted only if home contact is provided.              
    phones: typing.Optional[typing.Optional[typing.List[Phone]]] = Field(None, alias='Phones')

    # Social security number of the employee.
    social_security_number: typing.Optional[typing.Optional[str]] = Field(None, alias='SocialSecurityNumber')

    # Date of birth of the employee following the ISO 8601 standard. Format: YYYY-MM-DDTHH:MM:SSZ  (ISO-8601 standard) 
    birth_date: typing.Optional[typing.Optional[datetime]] = Field(None, alias='BirthDate')

    gender: typing.Optional[Gender] = Field(None, alias='Gender')

    ethnicity: typing.Optional[EthnicityType] = Field(None, alias='Ethnicity')

    marital_status: typing.Optional[MaritalStatus] = Field(None, alias='MaritalStatus')

    # The name of the Work Location to associate with new hire.  * Must be an existing Work Location. Use API 'GET Legal Entity Work Location by Legal Entity ID' to retrieve a list of valid names.             
    work_location: typing.Optional[typing.Optional[str]] = Field(None, alias='WorkLocation')

    # Name of the Job Title to associate with new hire.  * Must be an existing Job setup on the Tenant. Use API 'GET Tenant Job Titles by TenantId' to retrieve a list of valid names.             
    job_title: typing.Optional[typing.Optional[str]] = Field(None, alias='JobTitle')

    # Re-hire date of the employee. Terminated employees can be rehired.  Format: YYYY-MM-DDTHH:MM:SSZ  (ISO-8601 standard) 
    re_hire_date: typing.Optional[typing.Optional[datetime]] = Field(None, alias='ReHireDate')

    flsa: typing.Optional[FlsaType] = Field(None, alias='Flsa')

    type: typing.Optional[EmploymentType] = Field(None, alias='Type')

    # Unique identifier of the manager in Paycor's system. Generated by Paycor.
    manager_emp_id: typing.Optional[typing.Optional[str]] = Field(None, alias='ManagerEmpId')

    veteran: typing.Optional[VeteranStatus] = Field(None, alias='Veteran')

    disability: typing.Optional[DisabilityStatus] = Field(None, alias='Disability')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
