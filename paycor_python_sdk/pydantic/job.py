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

from paycor_python_sdk.pydantic.job_department import JobDepartment
from paycor_python_sdk.pydantic.job_location import JobLocation
from paycor_python_sdk.pydantic.job_pay_range import JobPayRange
from paycor_python_sdk.pydantic.job_priority import JobPriority
from paycor_python_sdk.pydantic.job_remote_status import JobRemoteStatus
from paycor_python_sdk.pydantic.job_status import JobStatus
from paycor_python_sdk.pydantic.job_user import JobUser

class Job(BaseModel):
    # Unique identifier of the Job in Paycor's system.
    id: typing.Optional[typing.Optional[str]] = Field(None, alias='Id')

    # The ATS client ID.
    a_t_s_account_id: typing.Optional[typing.Optional[str]] = Field(None, alias='ATSAccountId')

    # The job's human readable job number.
    number: typing.Optional[typing.Optional[str]] = Field(None, alias='Number')

    # The job's name.
    title: typing.Optional[typing.Optional[str]] = Field(None, alias='Title')

    # The job's description in HTML format.
    description: typing.Optional[typing.Optional[str]] = Field(None, alias='Description')

    status: typing.Optional[JobStatus] = Field(None, alias='Status')

    # The number of openings for the job.
    openings: typing.Optional[int] = Field(None, alias='Openings')

    priority: typing.Optional[JobPriority] = Field(None, alias='Priority')

    # If the job is confidential.
    confidential: typing.Optional[bool] = Field(None, alias='Confidential')

    # If the job is an internal only job.
    internal: typing.Optional[bool] = Field(None, alias='Internal')

    # The targeted time to fill the job.
    time_to_fill: typing.Optional[int] = Field(None, alias='TimeToFill')

    remote_status: typing.Optional[JobRemoteStatus] = Field(None, alias='RemoteStatus')

    # The EEO (Equal Employment Opportunity) category specification for the job. Can be one of these values: Executive/Senior-Level Officials and Managers, First/Mid-Level Officials and Managers, Professionals, Technicians, Sales Workers, Administrative Support Workers, Craft Workers, Operatives, Laborers and Helpers, Service Workers.
    eeo_category: typing.Optional[typing.Optional[str]] = Field(None, alias='EeoCategory')

    pay_range: typing.Optional[JobPayRange] = Field(None, alias='PayRange')

    a_t_s_location: typing.Optional[JobLocation] = Field(None, alias='ATSLocation')

    a_t_s_department: typing.Optional[JobDepartment] = Field(None, alias='ATSDepartment')

    # The hiring managers assigned to the job.
    hiring_managers: typing.Optional[typing.Optional[typing.List[JobUser]]] = Field(None, alias='HiringManagers')

    # The recruiters assigned to the job.
    recruiters: typing.Optional[typing.Optional[typing.List[JobUser]]] = Field(None, alias='Recruiters')

    # The team members assigned to the job.
    team_members: typing.Optional[typing.Optional[typing.List[JobUser]]] = Field(None, alias='TeamMembers')

    # The executives assigned to the job.
    executives: typing.Optional[typing.Optional[typing.List[JobUser]]] = Field(None, alias='Executives')

    # The date when the job was activated.
    activated_date: typing.Optional[typing.Optional[datetime]] = Field(None, alias='ActivatedDate')

    # The date when the job was created.
    created_date: typing.Optional[datetime] = Field(None, alias='CreatedDate')

    # The date when the job was last modified.
    modified_date: typing.Optional[datetime] = Field(None, alias='ModifiedDate')

    # Is the job posted to the company careers page.
    posted_to_careers: typing.Optional[bool] = Field(None, alias='PostedToCareers')

    # Is the job posted to the free Indeed feed.
    posted_to_indeed: typing.Optional[bool] = Field(None, alias='PostedToIndeed')

    # Is the job posted to Smart Sourcing.
    posted_to_smart_sourcing: typing.Optional[bool] = Field(None, alias='PostedToSmartSourcing')

    # Is the job posted to the free LinkedIn.
    posted_to_linked_in: typing.Optional[bool] = Field(None, alias='PostedToLinkedIn')

    # Is the job posted to the free ZipRecruiter feed.
    posted_to_zip_recruiter: typing.Optional[bool] = Field(None, alias='PostedToZipRecruiter')

    # Is the job posted to Gravity.             
    posted_to_gravity: typing.Optional[bool] = Field(None, alias='PostedToGravity')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
