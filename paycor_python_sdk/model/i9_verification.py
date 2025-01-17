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


class I9Verification(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class CitizenOfCountry(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'CitizenOfCountry':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def WorkEligibility() -> typing.Type['WorkEligibility']:
                return WorkEligibility
            
            
            class WorkVisaType(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'WorkVisaType':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class WorkVisaExpirationDate(
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
                ) -> 'WorkVisaExpirationDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class AlienAdmissionNumber(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'AlienAdmissionNumber':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class AlienAdmissionExpirationDate(
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
                ) -> 'AlienAdmissionExpirationDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def ListA() -> typing.Type['ListA']:
                return ListA
        
            @staticmethod
            def ListB() -> typing.Type['ListB']:
                return ListB
        
            @staticmethod
            def ListC() -> typing.Type['ListC']:
                return ListC
            
            
            class ForeignPassportNumber(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ForeignPassportNumber':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class CountryOfIssuance(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'CountryOfIssuance':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class AdditionalInformation(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'AdditionalInformation':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            HireDate = schemas.DateTimeSchema
            DateModified = schemas.DateTimeSchema
            __annotations__ = {
                "CitizenOfCountry": CitizenOfCountry,
                "WorkEligibility": WorkEligibility,
                "WorkVisaType": WorkVisaType,
                "WorkVisaExpirationDate": WorkVisaExpirationDate,
                "AlienAdmissionNumber": AlienAdmissionNumber,
                "AlienAdmissionExpirationDate": AlienAdmissionExpirationDate,
                "ListA": ListA,
                "ListB": ListB,
                "ListC": ListC,
                "ForeignPassportNumber": ForeignPassportNumber,
                "CountryOfIssuance": CountryOfIssuance,
                "AdditionalInformation": AdditionalInformation,
                "HireDate": HireDate,
                "DateModified": DateModified,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CitizenOfCountry"]) -> MetaOapg.properties.CitizenOfCountry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["WorkEligibility"]) -> 'WorkEligibility': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["WorkVisaType"]) -> MetaOapg.properties.WorkVisaType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["WorkVisaExpirationDate"]) -> MetaOapg.properties.WorkVisaExpirationDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AlienAdmissionNumber"]) -> MetaOapg.properties.AlienAdmissionNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AlienAdmissionExpirationDate"]) -> MetaOapg.properties.AlienAdmissionExpirationDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ListA"]) -> 'ListA': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ListB"]) -> 'ListB': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ListC"]) -> 'ListC': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ForeignPassportNumber"]) -> MetaOapg.properties.ForeignPassportNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CountryOfIssuance"]) -> MetaOapg.properties.CountryOfIssuance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AdditionalInformation"]) -> MetaOapg.properties.AdditionalInformation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["HireDate"]) -> MetaOapg.properties.HireDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DateModified"]) -> MetaOapg.properties.DateModified: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["CitizenOfCountry", "WorkEligibility", "WorkVisaType", "WorkVisaExpirationDate", "AlienAdmissionNumber", "AlienAdmissionExpirationDate", "ListA", "ListB", "ListC", "ForeignPassportNumber", "CountryOfIssuance", "AdditionalInformation", "HireDate", "DateModified", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CitizenOfCountry"]) -> typing.Union[MetaOapg.properties.CitizenOfCountry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["WorkEligibility"]) -> typing.Union['WorkEligibility', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["WorkVisaType"]) -> typing.Union[MetaOapg.properties.WorkVisaType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["WorkVisaExpirationDate"]) -> typing.Union[MetaOapg.properties.WorkVisaExpirationDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AlienAdmissionNumber"]) -> typing.Union[MetaOapg.properties.AlienAdmissionNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AlienAdmissionExpirationDate"]) -> typing.Union[MetaOapg.properties.AlienAdmissionExpirationDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ListA"]) -> typing.Union['ListA', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ListB"]) -> typing.Union['ListB', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ListC"]) -> typing.Union['ListC', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ForeignPassportNumber"]) -> typing.Union[MetaOapg.properties.ForeignPassportNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CountryOfIssuance"]) -> typing.Union[MetaOapg.properties.CountryOfIssuance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AdditionalInformation"]) -> typing.Union[MetaOapg.properties.AdditionalInformation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["HireDate"]) -> typing.Union[MetaOapg.properties.HireDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DateModified"]) -> typing.Union[MetaOapg.properties.DateModified, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["CitizenOfCountry", "WorkEligibility", "WorkVisaType", "WorkVisaExpirationDate", "AlienAdmissionNumber", "AlienAdmissionExpirationDate", "ListA", "ListB", "ListC", "ForeignPassportNumber", "CountryOfIssuance", "AdditionalInformation", "HireDate", "DateModified", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        CitizenOfCountry: typing.Union[MetaOapg.properties.CitizenOfCountry, None, str, schemas.Unset] = schemas.unset,
        WorkEligibility: typing.Union['WorkEligibility', schemas.Unset] = schemas.unset,
        WorkVisaType: typing.Union[MetaOapg.properties.WorkVisaType, None, str, schemas.Unset] = schemas.unset,
        WorkVisaExpirationDate: typing.Union[MetaOapg.properties.WorkVisaExpirationDate, None, str, datetime, schemas.Unset] = schemas.unset,
        AlienAdmissionNumber: typing.Union[MetaOapg.properties.AlienAdmissionNumber, None, str, schemas.Unset] = schemas.unset,
        AlienAdmissionExpirationDate: typing.Union[MetaOapg.properties.AlienAdmissionExpirationDate, None, str, datetime, schemas.Unset] = schemas.unset,
        ListA: typing.Union['ListA', schemas.Unset] = schemas.unset,
        ListB: typing.Union['ListB', schemas.Unset] = schemas.unset,
        ListC: typing.Union['ListC', schemas.Unset] = schemas.unset,
        ForeignPassportNumber: typing.Union[MetaOapg.properties.ForeignPassportNumber, None, str, schemas.Unset] = schemas.unset,
        CountryOfIssuance: typing.Union[MetaOapg.properties.CountryOfIssuance, None, str, schemas.Unset] = schemas.unset,
        AdditionalInformation: typing.Union[MetaOapg.properties.AdditionalInformation, None, str, schemas.Unset] = schemas.unset,
        HireDate: typing.Union[MetaOapg.properties.HireDate, str, datetime, schemas.Unset] = schemas.unset,
        DateModified: typing.Union[MetaOapg.properties.DateModified, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'I9Verification':
        return super().__new__(
            cls,
            *args,
            CitizenOfCountry=CitizenOfCountry,
            WorkEligibility=WorkEligibility,
            WorkVisaType=WorkVisaType,
            WorkVisaExpirationDate=WorkVisaExpirationDate,
            AlienAdmissionNumber=AlienAdmissionNumber,
            AlienAdmissionExpirationDate=AlienAdmissionExpirationDate,
            ListA=ListA,
            ListB=ListB,
            ListC=ListC,
            ForeignPassportNumber=ForeignPassportNumber,
            CountryOfIssuance=CountryOfIssuance,
            AdditionalInformation=AdditionalInformation,
            HireDate=HireDate,
            DateModified=DateModified,
            _configuration=_configuration,
            **kwargs,
        )

from paycor_python_sdk.model.list_a import ListA
from paycor_python_sdk.model.list_b import ListB
from paycor_python_sdk.model.list_c import ListC
from paycor_python_sdk.model.work_eligibility import WorkEligibility
