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


class PayGroup(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            LegalEntityId = schemas.Int32Schema
            PayrollId = schemas.StrSchema
            
            
            class PayrollDescription(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'PayrollDescription':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class PayrollCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'PayrollCode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            PayGroupId = schemas.StrSchema
            
            
            class PayGroupName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'PayGroupName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class PayGroupFrequency(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'PayGroupFrequency':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "LegalEntityId": LegalEntityId,
                "PayrollId": PayrollId,
                "PayrollDescription": PayrollDescription,
                "PayrollCode": PayrollCode,
                "PayGroupId": PayGroupId,
                "PayGroupName": PayGroupName,
                "PayGroupFrequency": PayGroupFrequency,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LegalEntityId"]) -> MetaOapg.properties.LegalEntityId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PayrollId"]) -> MetaOapg.properties.PayrollId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PayrollDescription"]) -> MetaOapg.properties.PayrollDescription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PayrollCode"]) -> MetaOapg.properties.PayrollCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PayGroupId"]) -> MetaOapg.properties.PayGroupId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PayGroupName"]) -> MetaOapg.properties.PayGroupName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PayGroupFrequency"]) -> MetaOapg.properties.PayGroupFrequency: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["LegalEntityId", "PayrollId", "PayrollDescription", "PayrollCode", "PayGroupId", "PayGroupName", "PayGroupFrequency", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LegalEntityId"]) -> typing.Union[MetaOapg.properties.LegalEntityId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PayrollId"]) -> typing.Union[MetaOapg.properties.PayrollId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PayrollDescription"]) -> typing.Union[MetaOapg.properties.PayrollDescription, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PayrollCode"]) -> typing.Union[MetaOapg.properties.PayrollCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PayGroupId"]) -> typing.Union[MetaOapg.properties.PayGroupId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PayGroupName"]) -> typing.Union[MetaOapg.properties.PayGroupName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PayGroupFrequency"]) -> typing.Union[MetaOapg.properties.PayGroupFrequency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["LegalEntityId", "PayrollId", "PayrollDescription", "PayrollCode", "PayGroupId", "PayGroupName", "PayGroupFrequency", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        LegalEntityId: typing.Union[MetaOapg.properties.LegalEntityId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        PayrollId: typing.Union[MetaOapg.properties.PayrollId, str, schemas.Unset] = schemas.unset,
        PayrollDescription: typing.Union[MetaOapg.properties.PayrollDescription, None, str, schemas.Unset] = schemas.unset,
        PayrollCode: typing.Union[MetaOapg.properties.PayrollCode, None, str, schemas.Unset] = schemas.unset,
        PayGroupId: typing.Union[MetaOapg.properties.PayGroupId, str, schemas.Unset] = schemas.unset,
        PayGroupName: typing.Union[MetaOapg.properties.PayGroupName, None, str, schemas.Unset] = schemas.unset,
        PayGroupFrequency: typing.Union[MetaOapg.properties.PayGroupFrequency, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PayGroup':
        return super().__new__(
            cls,
            *args,
            LegalEntityId=LegalEntityId,
            PayrollId=PayrollId,
            PayrollDescription=PayrollDescription,
            PayrollCode=PayrollCode,
            PayGroupId=PayGroupId,
            PayGroupName=PayGroupName,
            PayGroupFrequency=PayGroupFrequency,
            _configuration=_configuration,
            **kwargs,
        )
