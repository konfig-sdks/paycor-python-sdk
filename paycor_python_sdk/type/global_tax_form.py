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

from paycor_python_sdk.type.filing_status import FilingStatus

class RequiredGlobalTaxForm(TypedDict):
    pass

class OptionalGlobalTaxForm(TypedDict, total=False):
    # Effective start date of withholding.
    EffectiveStartDate: typing.Optional[datetime]

    # Effective end date of withholding.
    EffectiveEndDate: typing.Optional[datetime]

    # Information whether global tax requires the Filing status.
    HasFilingStatus: bool

    # Information whether global tax requires the adjust witholding field.
    HasAdjustWithholding: bool

    # Information whether global tax requires the override witholding date field.
    HasOverrideWithholdingDate: bool

    # Information whether global tax requires the applicable birth year field.
    HasApplicableBirthYear: bool

    # Information whether global tax requires the amount field.
    HasAmount: bool

    # Information whether global tax requires the rate field.
    HasRate: bool

    # Information whether global tax requires exemption amount field.
    HasExemptionAmount: bool

    # Information whether global tax requires non resident alien field.
    HasNonResidentAlien: bool

    # Information whether global tax requires the number of qualified dependents field.
    HasNumberOfQualifiedDependents: bool

    # Information whether global tax requires the Number Of Other Dependents field.
    HasNumberOfOtherDependents: bool

    # Information whether global tax requires the Number Of Exemptions field.
    HasNumberOfExemptions: bool

    # Information whether global tax requires the Spouse Working field.
    HasSpouseWorking: bool

    # Information whether global tax requires the HasTwoIncomes field.
    HasTwoIncomes: bool

    # Information whether global tax requires the AdditionalIncome field. Amount of employee's additional income as specified on employee's IRS Form W-4.
    HasAdditionalIncome: bool

    # Information whether global tax requires the Additional Deduction field.
    HasAdditionalDeduction: bool

    # Information whether global tax requires the Accuracy Confirmation field.
    HasAccuracyConfirmation: bool

    # Information whether global tax requires the Qualified Dependent Credit field.
    HasQualifiedDependentCredit: bool

    # Information whether global tax requires the Other Dependent Credit field.
    HasOtherDependentCredit: bool

    # Information whether global tax requires Total Credits field.
    HasTotalCredits: bool

    # Information whether global tax requires Qualified Dependent Credit field.
    QualifiedDependentCredit: typing.Optional[typing.Union[int, float]]

    # Information whether global tax requires Other Dependent Credit field.
    OtherDependentCredit: typing.Optional[typing.Union[int, float]]

    # Enumeration of valid filing status values for this tax code.
    FilingStatuses: typing.Optional[typing.List[FilingStatus]]

    # Information whether global tax requires the Income Tax field.
    HasIncomeTax: typing.Optional[str]

class GlobalTaxForm(RequiredGlobalTaxForm, OptionalGlobalTaxForm):
    pass
