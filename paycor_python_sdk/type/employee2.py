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

from paycor_python_sdk.type.disability_status import DisabilityStatus
from paycor_python_sdk.type.employment_status import EmploymentStatus
from paycor_python_sdk.type.employment_type import EmploymentType
from paycor_python_sdk.type.ethnicity_type import EthnicityType
from paycor_python_sdk.type.flsa_type import FlsaType
from paycor_python_sdk.type.gender import Gender
from paycor_python_sdk.type.generic_address import GenericAddress
from paycor_python_sdk.type.marital_status import MaritalStatus
from paycor_python_sdk.type.phone import Phone
from paycor_python_sdk.type.prefix import Prefix
from paycor_python_sdk.type.suffix import Suffix
from paycor_python_sdk.type.veteran_status import VeteranStatus

class RequiredEmployee2(TypedDict):
    # Employee's LegalEntityId.             
    LegalEntityId: int

    # First name of the employee.
    FirstName: str

    # Last name of the employee.
    LastName: str

    # Date the employee was hired following the ISO 8601 standard.. Format: YYYY-MM-DDTHH:MM:SSZ  (ISO-8601 standard)              
    HireDate: datetime

    Status: EmploymentStatus

    # The description of the paygroup that the employee belongs to.  * Must be existing Paygroup. Call GET Pay Groups by LegalEntityID to lookup valid values in the field \"PaygroupName\".              
    PaygroupDescription: str

    # The department code that the employee belongs to.   * Must be existing Department. Call Get Legal Entity Departments by LegalEntityID to get valid Code value.             
    DepartmentCode: int

    PrimaryAddress: GenericAddress

class OptionalEmployee2(TypedDict, total=False):
    # Unique number of the employee in the tenant. Generated by Paycor if not provided.             
    EmployeeNumber: typing.Optional[int]

    # Can be up to 9 characters, Requires Alternate Employee Number product offering.
    AlternateEmployeeNumber: typing.Optional[str]

    Prefix: Prefix

    # Middle name of the employee.
    MiddleName: typing.Optional[str]

    Suffix: Suffix

    # Home Email Information of an employee.             
    HomeEmail: typing.Optional[str]

    # Work Email Information of an employee.             
    WorkEmail: typing.Optional[str]

    # List of type Phone containing phone numbers of the employee. Accepts home,mobile and work phone numbers, upto 1 of each type. Mobile phone is accepted only if home contact is provided.              
    Phones: typing.Optional[typing.List[Phone]]

    # Social security number of the employee.
    SocialSecurityNumber: typing.Optional[str]

    # Date of birth of the employee following the ISO 8601 standard. Format: YYYY-MM-DDTHH:MM:SSZ  (ISO-8601 standard) 
    BirthDate: typing.Optional[datetime]

    Gender: Gender

    Ethnicity: EthnicityType

    MaritalStatus: MaritalStatus

    # The name of the Work Location to associate with new hire.  * Must be an existing Work Location. Use API 'GET Legal Entity Work Location by Legal Entity ID' to retrieve a list of valid names.             
    WorkLocation: typing.Optional[str]

    # Name of the Job Title to associate with new hire.  * Must be an existing Job setup on the Tenant. Use API 'GET Tenant Job Titles by TenantId' to retrieve a list of valid names.             
    JobTitle: typing.Optional[str]

    # Re-hire date of the employee. Terminated employees can be rehired.  Format: YYYY-MM-DDTHH:MM:SSZ  (ISO-8601 standard) 
    ReHireDate: typing.Optional[datetime]

    Flsa: FlsaType

    Type: EmploymentType

    # Unique identifier of the manager in Paycor's system. Generated by Paycor.
    ManagerEmpId: typing.Optional[str]

    Veteran: VeteranStatus

    Disability: DisabilityStatus

class Employee2(RequiredEmployee2, OptionalEmployee2):
    pass
