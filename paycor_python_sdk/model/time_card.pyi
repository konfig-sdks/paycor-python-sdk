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


class TimeCard(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The Timecard model represents Employee level time, punch details and associated labor code information. 
    """


    class MetaOapg:
        
        class properties:
            DisplayDate = schemas.DateTimeSchema
            
            
            class InActualPunch(
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
                ) -> 'InActualPunch':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class OutActualPunch(
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
                ) -> 'OutActualPunch':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class InRoundedPunch(
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
                ) -> 'InRoundedPunch':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class OutRoundedPunch(
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
                ) -> 'OutRoundedPunch':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            HoursAmount = schemas.NumberSchema
            DepartmentCode = schemas.Int64Schema
            
            
            class DepartmentName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'DepartmentName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class EarningCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'EarningCode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class LaborCodes(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['LaborCode2']:
                        return LaborCode2
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'LaborCodes':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "DisplayDate": DisplayDate,
                "InActualPunch": InActualPunch,
                "OutActualPunch": OutActualPunch,
                "InRoundedPunch": InRoundedPunch,
                "OutRoundedPunch": OutRoundedPunch,
                "HoursAmount": HoursAmount,
                "DepartmentCode": DepartmentCode,
                "DepartmentName": DepartmentName,
                "EarningCode": EarningCode,
                "LaborCodes": LaborCodes,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DisplayDate"]) -> MetaOapg.properties.DisplayDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["InActualPunch"]) -> MetaOapg.properties.InActualPunch: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OutActualPunch"]) -> MetaOapg.properties.OutActualPunch: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["InRoundedPunch"]) -> MetaOapg.properties.InRoundedPunch: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OutRoundedPunch"]) -> MetaOapg.properties.OutRoundedPunch: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["HoursAmount"]) -> MetaOapg.properties.HoursAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DepartmentCode"]) -> MetaOapg.properties.DepartmentCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DepartmentName"]) -> MetaOapg.properties.DepartmentName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EarningCode"]) -> MetaOapg.properties.EarningCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LaborCodes"]) -> MetaOapg.properties.LaborCodes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["DisplayDate", "InActualPunch", "OutActualPunch", "InRoundedPunch", "OutRoundedPunch", "HoursAmount", "DepartmentCode", "DepartmentName", "EarningCode", "LaborCodes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DisplayDate"]) -> typing.Union[MetaOapg.properties.DisplayDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["InActualPunch"]) -> typing.Union[MetaOapg.properties.InActualPunch, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OutActualPunch"]) -> typing.Union[MetaOapg.properties.OutActualPunch, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["InRoundedPunch"]) -> typing.Union[MetaOapg.properties.InRoundedPunch, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OutRoundedPunch"]) -> typing.Union[MetaOapg.properties.OutRoundedPunch, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["HoursAmount"]) -> typing.Union[MetaOapg.properties.HoursAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DepartmentCode"]) -> typing.Union[MetaOapg.properties.DepartmentCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DepartmentName"]) -> typing.Union[MetaOapg.properties.DepartmentName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EarningCode"]) -> typing.Union[MetaOapg.properties.EarningCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LaborCodes"]) -> typing.Union[MetaOapg.properties.LaborCodes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["DisplayDate", "InActualPunch", "OutActualPunch", "InRoundedPunch", "OutRoundedPunch", "HoursAmount", "DepartmentCode", "DepartmentName", "EarningCode", "LaborCodes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        DisplayDate: typing.Union[MetaOapg.properties.DisplayDate, str, datetime, schemas.Unset] = schemas.unset,
        InActualPunch: typing.Union[MetaOapg.properties.InActualPunch, None, str, datetime, schemas.Unset] = schemas.unset,
        OutActualPunch: typing.Union[MetaOapg.properties.OutActualPunch, None, str, datetime, schemas.Unset] = schemas.unset,
        InRoundedPunch: typing.Union[MetaOapg.properties.InRoundedPunch, None, str, datetime, schemas.Unset] = schemas.unset,
        OutRoundedPunch: typing.Union[MetaOapg.properties.OutRoundedPunch, None, str, datetime, schemas.Unset] = schemas.unset,
        HoursAmount: typing.Union[MetaOapg.properties.HoursAmount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        DepartmentCode: typing.Union[MetaOapg.properties.DepartmentCode, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        DepartmentName: typing.Union[MetaOapg.properties.DepartmentName, None, str, schemas.Unset] = schemas.unset,
        EarningCode: typing.Union[MetaOapg.properties.EarningCode, None, str, schemas.Unset] = schemas.unset,
        LaborCodes: typing.Union[MetaOapg.properties.LaborCodes, list, tuple, None, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TimeCard':
        return super().__new__(
            cls,
            *args,
            DisplayDate=DisplayDate,
            InActualPunch=InActualPunch,
            OutActualPunch=OutActualPunch,
            InRoundedPunch=InRoundedPunch,
            OutRoundedPunch=OutRoundedPunch,
            HoursAmount=HoursAmount,
            DepartmentCode=DepartmentCode,
            DepartmentName=DepartmentName,
            EarningCode=EarningCode,
            LaborCodes=LaborCodes,
            _configuration=_configuration,
            **kwargs,
        )

from paycor_python_sdk.model.labor_code2 import LaborCode2