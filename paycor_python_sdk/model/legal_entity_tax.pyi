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


class LegalEntityTax(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The Legal Entity (Client) tax model represents organization Legal Entity Tax information.  
    """


    class MetaOapg:
        
        class properties:
            LegalEntityTaxId = schemas.StrSchema
            LegalEntityId = schemas.Int32Schema
            
            
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
            def Type() -> typing.Type['TaxType']:
                return TaxType
            
            
            class TaxAuthCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'TaxAuthCode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def DepositFrequency() -> typing.Type['DepositFrequencyType']:
                return DepositFrequencyType
            
            
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
            
            
            class Rate(
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
                ) -> 'Rate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def ReciprocityType() -> typing.Type['ReciprocityType']:
                return ReciprocityType
            
            
            class OfferDependentInsurance(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'OfferDependentInsurance':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class WagePlan(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'WagePlan':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class ItemHold(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ItemHold':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def LegalEntity() -> typing.Type['ResourceReference']:
                return ResourceReference
            __annotations__ = {
                "LegalEntityTaxId": LegalEntityTaxId,
                "LegalEntityId": LegalEntityId,
                "TaxCode": TaxCode,
                "Description": Description,
                "Type": Type,
                "TaxAuthCode": TaxAuthCode,
                "DepositFrequency": DepositFrequency,
                "EffectiveStartDate": EffectiveStartDate,
                "SequenceNumber": SequenceNumber,
                "Rate": Rate,
                "ReciprocityType": ReciprocityType,
                "OfferDependentInsurance": OfferDependentInsurance,
                "WagePlan": WagePlan,
                "ItemHold": ItemHold,
                "LegalEntity": LegalEntity,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LegalEntityTaxId"]) -> MetaOapg.properties.LegalEntityTaxId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LegalEntityId"]) -> MetaOapg.properties.LegalEntityId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TaxCode"]) -> MetaOapg.properties.TaxCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Description"]) -> MetaOapg.properties.Description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Type"]) -> 'TaxType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TaxAuthCode"]) -> MetaOapg.properties.TaxAuthCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DepositFrequency"]) -> 'DepositFrequencyType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EffectiveStartDate"]) -> MetaOapg.properties.EffectiveStartDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SequenceNumber"]) -> MetaOapg.properties.SequenceNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Rate"]) -> MetaOapg.properties.Rate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ReciprocityType"]) -> 'ReciprocityType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OfferDependentInsurance"]) -> MetaOapg.properties.OfferDependentInsurance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["WagePlan"]) -> MetaOapg.properties.WagePlan: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ItemHold"]) -> MetaOapg.properties.ItemHold: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LegalEntity"]) -> 'ResourceReference': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["LegalEntityTaxId", "LegalEntityId", "TaxCode", "Description", "Type", "TaxAuthCode", "DepositFrequency", "EffectiveStartDate", "SequenceNumber", "Rate", "ReciprocityType", "OfferDependentInsurance", "WagePlan", "ItemHold", "LegalEntity", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LegalEntityTaxId"]) -> typing.Union[MetaOapg.properties.LegalEntityTaxId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LegalEntityId"]) -> typing.Union[MetaOapg.properties.LegalEntityId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TaxCode"]) -> typing.Union[MetaOapg.properties.TaxCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Description"]) -> typing.Union[MetaOapg.properties.Description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Type"]) -> typing.Union['TaxType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TaxAuthCode"]) -> typing.Union[MetaOapg.properties.TaxAuthCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DepositFrequency"]) -> typing.Union['DepositFrequencyType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EffectiveStartDate"]) -> typing.Union[MetaOapg.properties.EffectiveStartDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SequenceNumber"]) -> typing.Union[MetaOapg.properties.SequenceNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Rate"]) -> typing.Union[MetaOapg.properties.Rate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ReciprocityType"]) -> typing.Union['ReciprocityType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OfferDependentInsurance"]) -> typing.Union[MetaOapg.properties.OfferDependentInsurance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["WagePlan"]) -> typing.Union[MetaOapg.properties.WagePlan, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ItemHold"]) -> typing.Union[MetaOapg.properties.ItemHold, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LegalEntity"]) -> typing.Union['ResourceReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["LegalEntityTaxId", "LegalEntityId", "TaxCode", "Description", "Type", "TaxAuthCode", "DepositFrequency", "EffectiveStartDate", "SequenceNumber", "Rate", "ReciprocityType", "OfferDependentInsurance", "WagePlan", "ItemHold", "LegalEntity", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        LegalEntityTaxId: typing.Union[MetaOapg.properties.LegalEntityTaxId, str, schemas.Unset] = schemas.unset,
        LegalEntityId: typing.Union[MetaOapg.properties.LegalEntityId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        TaxCode: typing.Union[MetaOapg.properties.TaxCode, None, str, schemas.Unset] = schemas.unset,
        Description: typing.Union[MetaOapg.properties.Description, None, str, schemas.Unset] = schemas.unset,
        Type: typing.Union['TaxType', schemas.Unset] = schemas.unset,
        TaxAuthCode: typing.Union[MetaOapg.properties.TaxAuthCode, None, str, schemas.Unset] = schemas.unset,
        DepositFrequency: typing.Union['DepositFrequencyType', schemas.Unset] = schemas.unset,
        EffectiveStartDate: typing.Union[MetaOapg.properties.EffectiveStartDate, None, str, datetime, schemas.Unset] = schemas.unset,
        SequenceNumber: typing.Union[MetaOapg.properties.SequenceNumber, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Rate: typing.Union[MetaOapg.properties.Rate, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        ReciprocityType: typing.Union['ReciprocityType', schemas.Unset] = schemas.unset,
        OfferDependentInsurance: typing.Union[MetaOapg.properties.OfferDependentInsurance, None, bool, schemas.Unset] = schemas.unset,
        WagePlan: typing.Union[MetaOapg.properties.WagePlan, None, str, schemas.Unset] = schemas.unset,
        ItemHold: typing.Union[MetaOapg.properties.ItemHold, None, str, schemas.Unset] = schemas.unset,
        LegalEntity: typing.Union['ResourceReference', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LegalEntityTax':
        return super().__new__(
            cls,
            *args,
            LegalEntityTaxId=LegalEntityTaxId,
            LegalEntityId=LegalEntityId,
            TaxCode=TaxCode,
            Description=Description,
            Type=Type,
            TaxAuthCode=TaxAuthCode,
            DepositFrequency=DepositFrequency,
            EffectiveStartDate=EffectiveStartDate,
            SequenceNumber=SequenceNumber,
            Rate=Rate,
            ReciprocityType=ReciprocityType,
            OfferDependentInsurance=OfferDependentInsurance,
            WagePlan=WagePlan,
            ItemHold=ItemHold,
            LegalEntity=LegalEntity,
            _configuration=_configuration,
            **kwargs,
        )

from paycor_python_sdk.model.deposit_frequency_type import DepositFrequencyType
from paycor_python_sdk.model.reciprocity_type import ReciprocityType
from paycor_python_sdk.model.resource_reference import ResourceReference
from paycor_python_sdk.model.tax_type import TaxType