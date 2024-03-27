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

from paycor_python_sdk.pydantic.benefit_data import BenefitData
from paycor_python_sdk.pydantic.demographic_data import DemographicData
from paycor_python_sdk.pydantic.emergency_contact_data import EmergencyContactData
from paycor_python_sdk.pydantic.employee_assignment import EmployeeAssignment
from paycor_python_sdk.pydantic.military_data import MilitaryData
from paycor_python_sdk.pydantic.person_address import PersonAddress
from paycor_python_sdk.pydantic.person_email import PersonEmail
from paycor_python_sdk.pydantic.phone import Phone
from paycor_python_sdk.pydantic.prefix import Prefix
from paycor_python_sdk.pydantic.resource_reference import ResourceReference
from paycor_python_sdk.pydantic.social_media_data import SocialMediaData
from paycor_python_sdk.pydantic.suffix import Suffix

class Person(BaseModel):
    # Unique identifier of the person in Paycor's system. Generated by Paycor.
    id: typing.Optional[str] = Field(None, alias='Id')

    prefix: typing.Optional[Prefix] = Field(None, alias='Prefix')

    # First name of the person. 
    first_name: typing.Optional[typing.Optional[str]] = Field(None, alias='FirstName')

    # Middle name of the person.
    middle_name: typing.Optional[typing.Optional[str]] = Field(None, alias='MiddleName')

    # Last name of the person.
    last_name: typing.Optional[typing.Optional[str]] = Field(None, alias='LastName')

    suffix: typing.Optional[Suffix] = Field(None, alias='Suffix')

    # First name used on the person's W-2 tax form.             
    legal_first_name: typing.Optional[typing.Optional[str]] = Field(None, alias='LegalFirstName')

    # Last name used on the person's W-2 tax form.             
    legal_last_name: typing.Optional[typing.Optional[str]] = Field(None, alias='LegalLastName')

    # Social security number of the person.
    social_security_number: typing.Optional[typing.Optional[str]] = Field(None, alias='SocialSecurityNumber')

    email: typing.Optional[PersonEmail] = Field(None, alias='Email')

    demographic_data: typing.Optional[DemographicData] = Field(None, alias='DemographicData')

    benefit_data: typing.Optional[BenefitData] = Field(None, alias='BenefitData')

    # List of type EmergencyContactData containing a Person's emergency contacts data. This data will only be available for Get Person (returns single Person object) APIs and will always be null for Get Persons (returns list of Person) APIs.
    emergency_contact_data: typing.Optional[typing.Optional[typing.List[EmergencyContactData]]] = Field(None, alias='EmergencyContactData')

    military_data: typing.Optional[MilitaryData] = Field(None, alias='MilitaryData')

    # List of type SocialMediaData containing the Person's social media information.              
    social_media_data: typing.Optional[typing.Optional[typing.List[SocialMediaData]]] = Field(None, alias='SocialMediaData')

    # List of type EmployeeAssignment containing the person's employee assignments.             
    employee_assignments: typing.Optional[typing.Optional[typing.List[EmployeeAssignment]]] = Field(None, alias='EmployeeAssignments')

    # List of type Address containing the person's addresses.             
    addresses: typing.Optional[typing.Optional[typing.List[PersonAddress]]] = Field(None, alias='Addresses')

    # List of type Phone containing the person's phone numbers.             
    phones: typing.Optional[typing.Optional[typing.List[Phone]]] = Field(None, alias='Phones')

    tenants: typing.Optional[ResourceReference] = Field(None, alias='Tenants')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )