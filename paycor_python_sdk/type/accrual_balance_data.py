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


class RequiredAccrualBalanceData(TypedDict):
    # Unique identifier of the Employee in Paycor's system. Generated by Paycor. Used for other GET endpoints. 
    EmployeeId: str

    # Id of the planner for this payment
    PlannerId: str

    # Description of the time off type linked to this plan (admin-configured)
    TimeOffTypeDescription: str

    # Total hours added from start year to date. This value is required and cannot be null.
    HoursAddedYTD: typing.Union[int, float]

    # Total hours deducted from start year to date. This value is required and cannot be null.
    HoursUsedYTD: typing.Union[int, float]

    # Employee’s current available balance. This value is required and cannot be null.
    AvailableBalance: typing.Union[int, float]

class OptionalAccrualBalanceData(TypedDict, total=False):
    # Pay number
    PayNumber: int

    # Period end date. Format: YYYY-MM-DDTHH:MM:SSZ  (ISO-8601 standard)              
    PeriodEndDate: typing.Optional[datetime]

    # Abbreviated code of the time off type linked to this plan (admin-configured)
    TimeOffTypeCode: typing.Optional[str]

    # Determines what information to print on the payroll paystub (1.AvailableBalanceAndYTD,2.AvailableBalance,3.NoPrint)
    PrintOption: typing.Optional[str]

    # Determines which payroll paystubs should be printed(1.AllPayStubs,2.RegularOnly,3.AdditionalOnly)
    PayrunTypesToInclude: typing.Optional[str]

    # The number of days after an employee’s hire date before the balance is printed on the paystub
    PrintDelayinDays: int

    # If there is a balance shortfall at the time of payroll (1.Warning,2.None,3.DoNotPay)
    ShortfallOption: typing.Optional[str]

    # Whether to print the employee’s current balance (Current) or balance at the end of the pay period (Pay Period End Date) on the paystub
    PrintBalancePaystubOption: typing.Optional[str]

    # The employee’s start of year balance
    StartingBalance: typing.Union[int, float]

    # Maximum hours that an employee is entitled to use in a year
    MaxEntitledBalance: typing.Union[int, float]

    # Hours remaining until maxEntitledBalance limit is reached
    RemainingEntitledBalance: typing.Union[int, float]

class AccrualBalanceData(RequiredAccrualBalanceData, OptionalAccrualBalanceData):
    pass
