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


class EmployeeTaxHistoryItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            Id = schemas.StrSchema
            
            
            class Name(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Name':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class EmployerTaxAmount(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'decimal'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'EmployerTaxAmount':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class EmployeeTaxAmount(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'decimal'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'EmployeeTaxAmount':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class TaxableWages(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'decimal'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'TaxableWages':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class TaxableExemptWages(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'decimal'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'TaxableExemptWages':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class TaxableExcessWages(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'decimal'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'TaxableExcessWages':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class TotalWages(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'decimal'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'TotalWages':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class TaxCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'TaxCode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class TaxDescription(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'TaxDescription':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class TaxAmount(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'decimal'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'TaxAmount':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "Id": Id,
                "Name": Name,
                "EmployerTaxAmount": EmployerTaxAmount,
                "EmployeeTaxAmount": EmployeeTaxAmount,
                "TaxableWages": TaxableWages,
                "TaxableExemptWages": TaxableExemptWages,
                "TaxableExcessWages": TaxableExcessWages,
                "TotalWages": TotalWages,
                "TaxCode": TaxCode,
                "TaxDescription": TaxDescription,
                "TaxAmount": TaxAmount,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Id"]) -> MetaOapg.properties.Id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Name"]) -> MetaOapg.properties.Name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EmployerTaxAmount"]) -> MetaOapg.properties.EmployerTaxAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EmployeeTaxAmount"]) -> MetaOapg.properties.EmployeeTaxAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TaxableWages"]) -> MetaOapg.properties.TaxableWages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TaxableExemptWages"]) -> MetaOapg.properties.TaxableExemptWages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TaxableExcessWages"]) -> MetaOapg.properties.TaxableExcessWages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TotalWages"]) -> MetaOapg.properties.TotalWages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TaxCode"]) -> MetaOapg.properties.TaxCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TaxDescription"]) -> MetaOapg.properties.TaxDescription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TaxAmount"]) -> MetaOapg.properties.TaxAmount: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Id", "Name", "EmployerTaxAmount", "EmployeeTaxAmount", "TaxableWages", "TaxableExemptWages", "TaxableExcessWages", "TotalWages", "TaxCode", "TaxDescription", "TaxAmount", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Id"]) -> typing.Union[MetaOapg.properties.Id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Name"]) -> typing.Union[MetaOapg.properties.Name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EmployerTaxAmount"]) -> typing.Union[MetaOapg.properties.EmployerTaxAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EmployeeTaxAmount"]) -> typing.Union[MetaOapg.properties.EmployeeTaxAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TaxableWages"]) -> typing.Union[MetaOapg.properties.TaxableWages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TaxableExemptWages"]) -> typing.Union[MetaOapg.properties.TaxableExemptWages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TaxableExcessWages"]) -> typing.Union[MetaOapg.properties.TaxableExcessWages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TotalWages"]) -> typing.Union[MetaOapg.properties.TotalWages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TaxCode"]) -> typing.Union[MetaOapg.properties.TaxCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TaxDescription"]) -> typing.Union[MetaOapg.properties.TaxDescription, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TaxAmount"]) -> typing.Union[MetaOapg.properties.TaxAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Id", "Name", "EmployerTaxAmount", "EmployeeTaxAmount", "TaxableWages", "TaxableExemptWages", "TaxableExcessWages", "TotalWages", "TaxCode", "TaxDescription", "TaxAmount", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Id: typing.Union[MetaOapg.properties.Id, str, schemas.Unset] = schemas.unset,
        Name: typing.Union[MetaOapg.properties.Name, None, str, schemas.Unset] = schemas.unset,
        EmployerTaxAmount: typing.Union[MetaOapg.properties.EmployerTaxAmount, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        EmployeeTaxAmount: typing.Union[MetaOapg.properties.EmployeeTaxAmount, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        TaxableWages: typing.Union[MetaOapg.properties.TaxableWages, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        TaxableExemptWages: typing.Union[MetaOapg.properties.TaxableExemptWages, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        TaxableExcessWages: typing.Union[MetaOapg.properties.TaxableExcessWages, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        TotalWages: typing.Union[MetaOapg.properties.TotalWages, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        TaxCode: typing.Union[MetaOapg.properties.TaxCode, None, str, schemas.Unset] = schemas.unset,
        TaxDescription: typing.Union[MetaOapg.properties.TaxDescription, None, str, schemas.Unset] = schemas.unset,
        TaxAmount: typing.Union[MetaOapg.properties.TaxAmount, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeeTaxHistoryItem':
        return super().__new__(
            cls,
            *args,
            Id=Id,
            Name=Name,
            EmployerTaxAmount=EmployerTaxAmount,
            EmployeeTaxAmount=EmployeeTaxAmount,
            TaxableWages=TaxableWages,
            TaxableExemptWages=TaxableExemptWages,
            TaxableExcessWages=TaxableExcessWages,
            TotalWages=TotalWages,
            TaxCode=TaxCode,
            TaxDescription=TaxDescription,
            TaxAmount=TaxAmount,
            _configuration=_configuration,
            **kwargs,
        )
