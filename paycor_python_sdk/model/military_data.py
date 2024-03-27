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


class MilitaryData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The Military Data model represents a Person's military information.
            
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def Veteran() -> typing.Type['VeteranStatus']:
                return VeteranStatus
            
            
            class DischargeDate(
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
                ) -> 'DischargeDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class IsArmedForcesServiceMedalVeteran(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'IsArmedForcesServiceMedalVeteran':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class IsDisabledVeteran(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'IsDisabledVeteran':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class IsOtherProtectedVeteran(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'IsOtherProtectedVeteran':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class IsRecentlySeparatedVeteran(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'IsRecentlySeparatedVeteran':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class IsVietnamEra(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'IsVietnamEra':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class IsSpecialDisabled(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'IsSpecialDisabled':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "Veteran": Veteran,
                "DischargeDate": DischargeDate,
                "IsArmedForcesServiceMedalVeteran": IsArmedForcesServiceMedalVeteran,
                "IsDisabledVeteran": IsDisabledVeteran,
                "IsOtherProtectedVeteran": IsOtherProtectedVeteran,
                "IsRecentlySeparatedVeteran": IsRecentlySeparatedVeteran,
                "IsVietnamEra": IsVietnamEra,
                "IsSpecialDisabled": IsSpecialDisabled,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Veteran"]) -> 'VeteranStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DischargeDate"]) -> MetaOapg.properties.DischargeDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IsArmedForcesServiceMedalVeteran"]) -> MetaOapg.properties.IsArmedForcesServiceMedalVeteran: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IsDisabledVeteran"]) -> MetaOapg.properties.IsDisabledVeteran: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IsOtherProtectedVeteran"]) -> MetaOapg.properties.IsOtherProtectedVeteran: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IsRecentlySeparatedVeteran"]) -> MetaOapg.properties.IsRecentlySeparatedVeteran: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IsVietnamEra"]) -> MetaOapg.properties.IsVietnamEra: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IsSpecialDisabled"]) -> MetaOapg.properties.IsSpecialDisabled: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Veteran", "DischargeDate", "IsArmedForcesServiceMedalVeteran", "IsDisabledVeteran", "IsOtherProtectedVeteran", "IsRecentlySeparatedVeteran", "IsVietnamEra", "IsSpecialDisabled", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Veteran"]) -> typing.Union['VeteranStatus', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DischargeDate"]) -> typing.Union[MetaOapg.properties.DischargeDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IsArmedForcesServiceMedalVeteran"]) -> typing.Union[MetaOapg.properties.IsArmedForcesServiceMedalVeteran, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IsDisabledVeteran"]) -> typing.Union[MetaOapg.properties.IsDisabledVeteran, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IsOtherProtectedVeteran"]) -> typing.Union[MetaOapg.properties.IsOtherProtectedVeteran, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IsRecentlySeparatedVeteran"]) -> typing.Union[MetaOapg.properties.IsRecentlySeparatedVeteran, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IsVietnamEra"]) -> typing.Union[MetaOapg.properties.IsVietnamEra, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IsSpecialDisabled"]) -> typing.Union[MetaOapg.properties.IsSpecialDisabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Veteran", "DischargeDate", "IsArmedForcesServiceMedalVeteran", "IsDisabledVeteran", "IsOtherProtectedVeteran", "IsRecentlySeparatedVeteran", "IsVietnamEra", "IsSpecialDisabled", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Veteran: typing.Union['VeteranStatus', schemas.Unset] = schemas.unset,
        DischargeDate: typing.Union[MetaOapg.properties.DischargeDate, None, str, datetime, schemas.Unset] = schemas.unset,
        IsArmedForcesServiceMedalVeteran: typing.Union[MetaOapg.properties.IsArmedForcesServiceMedalVeteran, None, bool, schemas.Unset] = schemas.unset,
        IsDisabledVeteran: typing.Union[MetaOapg.properties.IsDisabledVeteran, None, bool, schemas.Unset] = schemas.unset,
        IsOtherProtectedVeteran: typing.Union[MetaOapg.properties.IsOtherProtectedVeteran, None, bool, schemas.Unset] = schemas.unset,
        IsRecentlySeparatedVeteran: typing.Union[MetaOapg.properties.IsRecentlySeparatedVeteran, None, bool, schemas.Unset] = schemas.unset,
        IsVietnamEra: typing.Union[MetaOapg.properties.IsVietnamEra, None, bool, schemas.Unset] = schemas.unset,
        IsSpecialDisabled: typing.Union[MetaOapg.properties.IsSpecialDisabled, None, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MilitaryData':
        return super().__new__(
            cls,
            *args,
            Veteran=Veteran,
            DischargeDate=DischargeDate,
            IsArmedForcesServiceMedalVeteran=IsArmedForcesServiceMedalVeteran,
            IsDisabledVeteran=IsDisabledVeteran,
            IsOtherProtectedVeteran=IsOtherProtectedVeteran,
            IsRecentlySeparatedVeteran=IsRecentlySeparatedVeteran,
            IsVietnamEra=IsVietnamEra,
            IsSpecialDisabled=IsSpecialDisabled,
            _configuration=_configuration,
            **kwargs,
        )

from paycor_python_sdk.model.veteran_status import VeteranStatus
