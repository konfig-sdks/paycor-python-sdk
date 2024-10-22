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


class EmployeeTaxCredit(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The Employee Tax Credit Model represents the Employee's Tax Credit information.
    """


    class MetaOapg:
        
        class properties:
            
            
            class NumberOfDependents(
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
                ) -> 'NumberOfDependents':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class NumberOfOtherDependents(
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
                ) -> 'NumberOfOtherDependents':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class HasTwoIncomes(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'HasTwoIncomes':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class AdditionalIncome(
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
                ) -> 'AdditionalIncome':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class AdditionalDeduction(
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
                ) -> 'AdditionalDeduction':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class QualifiedDependentCredit(
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
                ) -> 'QualifiedDependentCredit':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class OtherDependentCredit(
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
                ) -> 'OtherDependentCredit':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class TotalCredits(
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
                ) -> 'TotalCredits':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "NumberOfDependents": NumberOfDependents,
                "NumberOfOtherDependents": NumberOfOtherDependents,
                "HasTwoIncomes": HasTwoIncomes,
                "AdditionalIncome": AdditionalIncome,
                "AdditionalDeduction": AdditionalDeduction,
                "QualifiedDependentCredit": QualifiedDependentCredit,
                "OtherDependentCredit": OtherDependentCredit,
                "TotalCredits": TotalCredits,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["NumberOfDependents"]) -> MetaOapg.properties.NumberOfDependents: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["NumberOfOtherDependents"]) -> MetaOapg.properties.NumberOfOtherDependents: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["HasTwoIncomes"]) -> MetaOapg.properties.HasTwoIncomes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AdditionalIncome"]) -> MetaOapg.properties.AdditionalIncome: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AdditionalDeduction"]) -> MetaOapg.properties.AdditionalDeduction: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["QualifiedDependentCredit"]) -> MetaOapg.properties.QualifiedDependentCredit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OtherDependentCredit"]) -> MetaOapg.properties.OtherDependentCredit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TotalCredits"]) -> MetaOapg.properties.TotalCredits: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["NumberOfDependents", "NumberOfOtherDependents", "HasTwoIncomes", "AdditionalIncome", "AdditionalDeduction", "QualifiedDependentCredit", "OtherDependentCredit", "TotalCredits", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["NumberOfDependents"]) -> typing.Union[MetaOapg.properties.NumberOfDependents, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["NumberOfOtherDependents"]) -> typing.Union[MetaOapg.properties.NumberOfOtherDependents, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["HasTwoIncomes"]) -> typing.Union[MetaOapg.properties.HasTwoIncomes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AdditionalIncome"]) -> typing.Union[MetaOapg.properties.AdditionalIncome, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AdditionalDeduction"]) -> typing.Union[MetaOapg.properties.AdditionalDeduction, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["QualifiedDependentCredit"]) -> typing.Union[MetaOapg.properties.QualifiedDependentCredit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OtherDependentCredit"]) -> typing.Union[MetaOapg.properties.OtherDependentCredit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TotalCredits"]) -> typing.Union[MetaOapg.properties.TotalCredits, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["NumberOfDependents", "NumberOfOtherDependents", "HasTwoIncomes", "AdditionalIncome", "AdditionalDeduction", "QualifiedDependentCredit", "OtherDependentCredit", "TotalCredits", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        NumberOfDependents: typing.Union[MetaOapg.properties.NumberOfDependents, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        NumberOfOtherDependents: typing.Union[MetaOapg.properties.NumberOfOtherDependents, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        HasTwoIncomes: typing.Union[MetaOapg.properties.HasTwoIncomes, None, bool, schemas.Unset] = schemas.unset,
        AdditionalIncome: typing.Union[MetaOapg.properties.AdditionalIncome, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        AdditionalDeduction: typing.Union[MetaOapg.properties.AdditionalDeduction, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        QualifiedDependentCredit: typing.Union[MetaOapg.properties.QualifiedDependentCredit, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        OtherDependentCredit: typing.Union[MetaOapg.properties.OtherDependentCredit, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        TotalCredits: typing.Union[MetaOapg.properties.TotalCredits, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeeTaxCredit':
        return super().__new__(
            cls,
            *args,
            NumberOfDependents=NumberOfDependents,
            NumberOfOtherDependents=NumberOfOtherDependents,
            HasTwoIncomes=HasTwoIncomes,
            AdditionalIncome=AdditionalIncome,
            AdditionalDeduction=AdditionalDeduction,
            QualifiedDependentCredit=QualifiedDependentCredit,
            OtherDependentCredit=OtherDependentCredit,
            TotalCredits=TotalCredits,
            _configuration=_configuration,
            **kwargs,
        )
