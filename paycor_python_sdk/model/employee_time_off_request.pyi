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


class EmployeeTimeOffRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Employee Time Off Request model represents information about time off requests for specific employee.
    """


    class MetaOapg:
        
        class properties:
            LegalEntityId = schemas.Int32Schema
            TimeOffRequestId = schemas.StrSchema
            
            
            class BenefitCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'BenefitCode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            TotalHours = schemas.NumberSchema
            
            
            class Days(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TimeOffRequestDay']:
                        return TimeOffRequestDay
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Days':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class Comment(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Comment':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class Status(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Status':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            CreatedDate = schemas.DateTimeSchema
            StatusUpdateTime = schemas.DateTimeSchema
            StatusUpdateByEmployeeId = schemas.StrSchema
            CreatedByEmployeeId = schemas.StrSchema
            EmployeeId = schemas.StrSchema
            __annotations__ = {
                "LegalEntityId": LegalEntityId,
                "TimeOffRequestId": TimeOffRequestId,
                "BenefitCode": BenefitCode,
                "TotalHours": TotalHours,
                "Days": Days,
                "Comment": Comment,
                "Status": Status,
                "CreatedDate": CreatedDate,
                "StatusUpdateTime": StatusUpdateTime,
                "StatusUpdateByEmployeeId": StatusUpdateByEmployeeId,
                "CreatedByEmployeeId": CreatedByEmployeeId,
                "EmployeeId": EmployeeId,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LegalEntityId"]) -> MetaOapg.properties.LegalEntityId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeOffRequestId"]) -> MetaOapg.properties.TimeOffRequestId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BenefitCode"]) -> MetaOapg.properties.BenefitCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TotalHours"]) -> MetaOapg.properties.TotalHours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Days"]) -> MetaOapg.properties.Days: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Comment"]) -> MetaOapg.properties.Comment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Status"]) -> MetaOapg.properties.Status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CreatedDate"]) -> MetaOapg.properties.CreatedDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StatusUpdateTime"]) -> MetaOapg.properties.StatusUpdateTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StatusUpdateByEmployeeId"]) -> MetaOapg.properties.StatusUpdateByEmployeeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CreatedByEmployeeId"]) -> MetaOapg.properties.CreatedByEmployeeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EmployeeId"]) -> MetaOapg.properties.EmployeeId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["LegalEntityId", "TimeOffRequestId", "BenefitCode", "TotalHours", "Days", "Comment", "Status", "CreatedDate", "StatusUpdateTime", "StatusUpdateByEmployeeId", "CreatedByEmployeeId", "EmployeeId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LegalEntityId"]) -> typing.Union[MetaOapg.properties.LegalEntityId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeOffRequestId"]) -> typing.Union[MetaOapg.properties.TimeOffRequestId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BenefitCode"]) -> typing.Union[MetaOapg.properties.BenefitCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TotalHours"]) -> typing.Union[MetaOapg.properties.TotalHours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Days"]) -> typing.Union[MetaOapg.properties.Days, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Comment"]) -> typing.Union[MetaOapg.properties.Comment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Status"]) -> typing.Union[MetaOapg.properties.Status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CreatedDate"]) -> typing.Union[MetaOapg.properties.CreatedDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StatusUpdateTime"]) -> typing.Union[MetaOapg.properties.StatusUpdateTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StatusUpdateByEmployeeId"]) -> typing.Union[MetaOapg.properties.StatusUpdateByEmployeeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CreatedByEmployeeId"]) -> typing.Union[MetaOapg.properties.CreatedByEmployeeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EmployeeId"]) -> typing.Union[MetaOapg.properties.EmployeeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["LegalEntityId", "TimeOffRequestId", "BenefitCode", "TotalHours", "Days", "Comment", "Status", "CreatedDate", "StatusUpdateTime", "StatusUpdateByEmployeeId", "CreatedByEmployeeId", "EmployeeId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        LegalEntityId: typing.Union[MetaOapg.properties.LegalEntityId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        TimeOffRequestId: typing.Union[MetaOapg.properties.TimeOffRequestId, str, schemas.Unset] = schemas.unset,
        BenefitCode: typing.Union[MetaOapg.properties.BenefitCode, None, str, schemas.Unset] = schemas.unset,
        TotalHours: typing.Union[MetaOapg.properties.TotalHours, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        Days: typing.Union[MetaOapg.properties.Days, list, tuple, None, schemas.Unset] = schemas.unset,
        Comment: typing.Union[MetaOapg.properties.Comment, None, str, schemas.Unset] = schemas.unset,
        Status: typing.Union[MetaOapg.properties.Status, None, str, schemas.Unset] = schemas.unset,
        CreatedDate: typing.Union[MetaOapg.properties.CreatedDate, str, datetime, schemas.Unset] = schemas.unset,
        StatusUpdateTime: typing.Union[MetaOapg.properties.StatusUpdateTime, str, datetime, schemas.Unset] = schemas.unset,
        StatusUpdateByEmployeeId: typing.Union[MetaOapg.properties.StatusUpdateByEmployeeId, str, schemas.Unset] = schemas.unset,
        CreatedByEmployeeId: typing.Union[MetaOapg.properties.CreatedByEmployeeId, str, schemas.Unset] = schemas.unset,
        EmployeeId: typing.Union[MetaOapg.properties.EmployeeId, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeeTimeOffRequest':
        return super().__new__(
            cls,
            *args,
            LegalEntityId=LegalEntityId,
            TimeOffRequestId=TimeOffRequestId,
            BenefitCode=BenefitCode,
            TotalHours=TotalHours,
            Days=Days,
            Comment=Comment,
            Status=Status,
            CreatedDate=CreatedDate,
            StatusUpdateTime=StatusUpdateTime,
            StatusUpdateByEmployeeId=StatusUpdateByEmployeeId,
            CreatedByEmployeeId=CreatedByEmployeeId,
            EmployeeId=EmployeeId,
            _configuration=_configuration,
            **kwargs,
        )

from paycor_python_sdk.model.time_off_request_day import TimeOffRequestDay
