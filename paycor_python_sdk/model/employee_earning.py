# coding: utf-8

"""
    Paycor Public API

     Welcome to Paycor's Public API! This document is a reference for the APIs Paycor has available, and acts as a complement to the \"Guides\" section.   # Getting Started  <strong>To learn more about getting started with Paycor's Public APIs, check out our <a href=\"/guides\">Guides.</a></strong>  # GET, PUT, POST  * When requesting object, use GET endpoints. All list endpoints support paging, as described [in the other doc].  * When creating an object, use POST endpoints. Your code will need to create an object and send it to Paycor in your API call request body as JSON. You can use the \"request sample\" body as a starting point. Our endpoints will return a reference to the created object (the ID and GET API URL) for your system. * When updating an object, you will use PUT endpoints. The general flow would be to: GET the object you want to update, modify the fields as desired, then PUT the object (as JSON in the request body) to our endpoints. Some fields like the object's ID cannot be updated because they are system-set.'   # Error Handling  * 400: Please consult the response text to correct your request information.  * 401 with response \"Access denied due to missing subscription key\": Please include your APIM Subscription Key as header Ocp-Apim-Subscription-Key or querystring parameter subscription-key.  * 401 with no response: Please ensure you included a valid & current Access Token in the Authorization header. * 403: Please ensure your Access Token's scope has all the relevant access you need, on the AppCreator Data Access screen.  * 404: Please validate the API route you are using. If that is correct, one of your IDs most likely does not exist or is not in a valid state.  * 429: Paycor implements rate limits for our Public API. Each customer (implemented via APIM subscription key) has a limited number of calls. The number of calls is counted across all APIs, not per individual API. Please use bulk endpoints where available and spread your calls over a wider timespan.   * The default rate limit is up to 1000 API calls per minute (total across all our Public APIs).  * 500: Please contact Paycor. When you make a POST or PUT call and receive a 500, please do not retry the call automatically - this may result in double-posting. GETs can be safely retried.   # IDs  * ClientId = LegalEntityId * TenantId = CompanyId * EmployeeId is not visible in Paycor's UI, you must retrieve it from the Public API  # Earnings, Deductions, Taxes  This section describes the domain model for Paycor's Earnings, Deductions, and Taxes. This will provide background for many paydata-related Public API endpoints.   Paycor stores Earnings, Deductions, and Taxes each at three levels: * Global: Same data across all legal entities. Setup by Paycor for customers to choose from. Sample Codes (note these will not be setup on every Legal Entity):   * Earnings: REG, OT   * Taxes: FITWH, SOC, SOCER, OHCIN   * Deductions: 401k, KMat, H125, UWay * Legal Entity or Tenant: Codes setup &amp; customized on the legal entity or Tenant level. Must be tied to a Global Code.    * Perform UI allows creating Deduction and Earning codes on Tenant level (under Configure Company nav menu). These will be returned by the Legal Entity Public API endpoints.  * Employee: codes setup on a particular employee, tied to a Legal Entity-level or Tenant-level code   * Employee Earnings/Deductions/Taxes are applied during payroll. Many properties are inherited from the Legal Entity or Global levels, but some can be overridden.   # Authentication  <!-- ReDoc-Inject: <security-definitions> -->

    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from paycor_python_sdk import schemas  # noqa: F401


class EmployeeEarning(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A record of one specific earning that one particular employee has setup, including employee-specific details such as amount. Must be tied to an earning at the LegalEntity level.
    """


    class MetaOapg:
        
        class properties:
            Id = schemas.StrSchema
            
            
            class Code(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Code':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class Description(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Description':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def Type() -> typing.Type['EarningType']:
                return EarningType
        
            @staticmethod
            def Frequency() -> typing.Type['PayFrequency']:
                return PayFrequency
            
            
            class SequenceNumber(
                schemas.Int32Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int32'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'SequenceNumber':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def IncludeInPay() -> typing.Type['IncludeInPay']:
                return IncludeInPay
            OnHold = schemas.BoolSchema
            
            
            class EffectiveStartDate(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'EffectiveStartDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class EffectiveEndDate(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'EffectiveEndDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class AmountData(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['EmployeeEarningAmount']:
                        return EmployeeEarningAmount
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'AmountData':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def Employee() -> typing.Type['ResourceReference']:
                return ResourceReference
        
            @staticmethod
            def LegalEntityEarning() -> typing.Type['ResourceReference']:
                return ResourceReference
            __annotations__ = {
                "Id": Id,
                "Code": Code,
                "Description": Description,
                "Type": Type,
                "Frequency": Frequency,
                "SequenceNumber": SequenceNumber,
                "IncludeInPay": IncludeInPay,
                "OnHold": OnHold,
                "EffectiveStartDate": EffectiveStartDate,
                "EffectiveEndDate": EffectiveEndDate,
                "AmountData": AmountData,
                "Employee": Employee,
                "LegalEntityEarning": LegalEntityEarning,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Id"]) -> MetaOapg.properties.Id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Code"]) -> MetaOapg.properties.Code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Description"]) -> MetaOapg.properties.Description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Type"]) -> 'EarningType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Frequency"]) -> 'PayFrequency': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SequenceNumber"]) -> MetaOapg.properties.SequenceNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IncludeInPay"]) -> 'IncludeInPay': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OnHold"]) -> MetaOapg.properties.OnHold: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EffectiveStartDate"]) -> MetaOapg.properties.EffectiveStartDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EffectiveEndDate"]) -> MetaOapg.properties.EffectiveEndDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AmountData"]) -> MetaOapg.properties.AmountData: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Employee"]) -> 'ResourceReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LegalEntityEarning"]) -> 'ResourceReference': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Id", "Code", "Description", "Type", "Frequency", "SequenceNumber", "IncludeInPay", "OnHold", "EffectiveStartDate", "EffectiveEndDate", "AmountData", "Employee", "LegalEntityEarning", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Id"]) -> typing.Union[MetaOapg.properties.Id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Code"]) -> typing.Union[MetaOapg.properties.Code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Description"]) -> typing.Union[MetaOapg.properties.Description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Type"]) -> typing.Union['EarningType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Frequency"]) -> typing.Union['PayFrequency', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SequenceNumber"]) -> typing.Union[MetaOapg.properties.SequenceNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IncludeInPay"]) -> typing.Union['IncludeInPay', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OnHold"]) -> typing.Union[MetaOapg.properties.OnHold, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EffectiveStartDate"]) -> typing.Union[MetaOapg.properties.EffectiveStartDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EffectiveEndDate"]) -> typing.Union[MetaOapg.properties.EffectiveEndDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AmountData"]) -> typing.Union[MetaOapg.properties.AmountData, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Employee"]) -> typing.Union['ResourceReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LegalEntityEarning"]) -> typing.Union['ResourceReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Id", "Code", "Description", "Type", "Frequency", "SequenceNumber", "IncludeInPay", "OnHold", "EffectiveStartDate", "EffectiveEndDate", "AmountData", "Employee", "LegalEntityEarning", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Id: typing.Union[MetaOapg.properties.Id, str, schemas.Unset] = schemas.unset,
        Code: typing.Union[MetaOapg.properties.Code, None, str, schemas.Unset] = schemas.unset,
        Description: typing.Union[MetaOapg.properties.Description, None, str, schemas.Unset] = schemas.unset,
        Type: typing.Union['EarningType', schemas.Unset] = schemas.unset,
        Frequency: typing.Union['PayFrequency', schemas.Unset] = schemas.unset,
        SequenceNumber: typing.Union[MetaOapg.properties.SequenceNumber, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        IncludeInPay: typing.Union['IncludeInPay', schemas.Unset] = schemas.unset,
        OnHold: typing.Union[MetaOapg.properties.OnHold, bool, schemas.Unset] = schemas.unset,
        EffectiveStartDate: typing.Union[MetaOapg.properties.EffectiveStartDate, None, str, datetime, schemas.Unset] = schemas.unset,
        EffectiveEndDate: typing.Union[MetaOapg.properties.EffectiveEndDate, None, str, datetime, schemas.Unset] = schemas.unset,
        AmountData: typing.Union[MetaOapg.properties.AmountData, list, tuple, None, schemas.Unset] = schemas.unset,
        Employee: typing.Union['ResourceReference', schemas.Unset] = schemas.unset,
        LegalEntityEarning: typing.Union['ResourceReference', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeeEarning':
        return super().__new__(
            cls,
            *args,
            Id=Id,
            Code=Code,
            Description=Description,
            Type=Type,
            Frequency=Frequency,
            SequenceNumber=SequenceNumber,
            IncludeInPay=IncludeInPay,
            OnHold=OnHold,
            EffectiveStartDate=EffectiveStartDate,
            EffectiveEndDate=EffectiveEndDate,
            AmountData=AmountData,
            Employee=Employee,
            LegalEntityEarning=LegalEntityEarning,
            _configuration=_configuration,
            **kwargs,
        )

from paycor_python_sdk.model.earning_type import EarningType
from paycor_python_sdk.model.employee_earning_amount import EmployeeEarningAmount
from paycor_python_sdk.model.include_in_pay import IncludeInPay
from paycor_python_sdk.model.pay_frequency import PayFrequency
from paycor_python_sdk.model.resource_reference import ResourceReference
