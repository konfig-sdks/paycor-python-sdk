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


class EmployeeTax3(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The Employee Tax model represents Employee level Tax information.
    """


    class MetaOapg:
        required = {
            "LegalEntityTaxId",
            "Id",
        }
        
        class properties:
            
            
            class Id(
                schemas.StrSchema
            ):
                pass
            
            
            class LegalEntityTaxId(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def ReciprocityType() -> typing.Type['ReciprocityType']:
                return ReciprocityType
        
            @staticmethod
            def FilingStatus() -> typing.Type['FilingStatus2']:
                return FilingStatus2
            
            
            class WithholdingEffectiveStartDate(
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
                ) -> 'WithholdingEffectiveStartDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class BlockDate(
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
                ) -> 'BlockDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class NonResidentAlien(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'NonResidentAlien':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class IsProbationaryEmployee(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'IsProbationaryEmployee':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class OccupationalCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'OccupationalCode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class GeographicCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'GeographicCode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class SOCCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'SOCCode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class SeasonalCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'SeasonalCode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class CountyCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'CountyCode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class SpouseWork(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'SpouseWork':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class DependentInsuranceEligible(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'DependentInsuranceEligible':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class DependentInsuranceEligibleDate(
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
                ) -> 'DependentInsuranceEligibleDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class ApplicableBirthyear(
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
                ) -> 'ApplicableBirthyear':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class Amount(
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
                ) -> 'Amount':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class Percentage(
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
                ) -> 'Percentage':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class NCCICode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'NCCICode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class PsdCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'PsdCode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class PsdRate(
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
                ) -> 'PsdRate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class OnHold(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'OnHold':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def Exemptions() -> typing.Type['EmployeeExemptions']:
                return EmployeeExemptions
        
            @staticmethod
            def TaxCredit() -> typing.Type['EmployeeTaxCredit']:
                return EmployeeTaxCredit
            __annotations__ = {
                "Id": Id,
                "LegalEntityTaxId": LegalEntityTaxId,
                "ReciprocityType": ReciprocityType,
                "FilingStatus": FilingStatus,
                "WithholdingEffectiveStartDate": WithholdingEffectiveStartDate,
                "BlockDate": BlockDate,
                "NonResidentAlien": NonResidentAlien,
                "IsProbationaryEmployee": IsProbationaryEmployee,
                "OccupationalCode": OccupationalCode,
                "GeographicCode": GeographicCode,
                "SOCCode": SOCCode,
                "SeasonalCode": SeasonalCode,
                "CountyCode": CountyCode,
                "SpouseWork": SpouseWork,
                "DependentInsuranceEligible": DependentInsuranceEligible,
                "DependentInsuranceEligibleDate": DependentInsuranceEligibleDate,
                "ApplicableBirthyear": ApplicableBirthyear,
                "Amount": Amount,
                "Percentage": Percentage,
                "NCCICode": NCCICode,
                "PsdCode": PsdCode,
                "PsdRate": PsdRate,
                "OnHold": OnHold,
                "Exemptions": Exemptions,
                "TaxCredit": TaxCredit,
            }
    
    LegalEntityTaxId: MetaOapg.properties.LegalEntityTaxId
    Id: MetaOapg.properties.Id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Id"]) -> MetaOapg.properties.Id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LegalEntityTaxId"]) -> MetaOapg.properties.LegalEntityTaxId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ReciprocityType"]) -> 'ReciprocityType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FilingStatus"]) -> 'FilingStatus2': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["WithholdingEffectiveStartDate"]) -> MetaOapg.properties.WithholdingEffectiveStartDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BlockDate"]) -> MetaOapg.properties.BlockDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["NonResidentAlien"]) -> MetaOapg.properties.NonResidentAlien: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IsProbationaryEmployee"]) -> MetaOapg.properties.IsProbationaryEmployee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OccupationalCode"]) -> MetaOapg.properties.OccupationalCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["GeographicCode"]) -> MetaOapg.properties.GeographicCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SOCCode"]) -> MetaOapg.properties.SOCCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SeasonalCode"]) -> MetaOapg.properties.SeasonalCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CountyCode"]) -> MetaOapg.properties.CountyCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SpouseWork"]) -> MetaOapg.properties.SpouseWork: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DependentInsuranceEligible"]) -> MetaOapg.properties.DependentInsuranceEligible: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DependentInsuranceEligibleDate"]) -> MetaOapg.properties.DependentInsuranceEligibleDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ApplicableBirthyear"]) -> MetaOapg.properties.ApplicableBirthyear: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Amount"]) -> MetaOapg.properties.Amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Percentage"]) -> MetaOapg.properties.Percentage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["NCCICode"]) -> MetaOapg.properties.NCCICode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PsdCode"]) -> MetaOapg.properties.PsdCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PsdRate"]) -> MetaOapg.properties.PsdRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OnHold"]) -> MetaOapg.properties.OnHold: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Exemptions"]) -> 'EmployeeExemptions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TaxCredit"]) -> 'EmployeeTaxCredit': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Id", "LegalEntityTaxId", "ReciprocityType", "FilingStatus", "WithholdingEffectiveStartDate", "BlockDate", "NonResidentAlien", "IsProbationaryEmployee", "OccupationalCode", "GeographicCode", "SOCCode", "SeasonalCode", "CountyCode", "SpouseWork", "DependentInsuranceEligible", "DependentInsuranceEligibleDate", "ApplicableBirthyear", "Amount", "Percentage", "NCCICode", "PsdCode", "PsdRate", "OnHold", "Exemptions", "TaxCredit", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Id"]) -> MetaOapg.properties.Id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LegalEntityTaxId"]) -> MetaOapg.properties.LegalEntityTaxId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ReciprocityType"]) -> typing.Union['ReciprocityType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FilingStatus"]) -> typing.Union['FilingStatus2', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["WithholdingEffectiveStartDate"]) -> typing.Union[MetaOapg.properties.WithholdingEffectiveStartDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BlockDate"]) -> typing.Union[MetaOapg.properties.BlockDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["NonResidentAlien"]) -> typing.Union[MetaOapg.properties.NonResidentAlien, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IsProbationaryEmployee"]) -> typing.Union[MetaOapg.properties.IsProbationaryEmployee, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OccupationalCode"]) -> typing.Union[MetaOapg.properties.OccupationalCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["GeographicCode"]) -> typing.Union[MetaOapg.properties.GeographicCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SOCCode"]) -> typing.Union[MetaOapg.properties.SOCCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SeasonalCode"]) -> typing.Union[MetaOapg.properties.SeasonalCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CountyCode"]) -> typing.Union[MetaOapg.properties.CountyCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SpouseWork"]) -> typing.Union[MetaOapg.properties.SpouseWork, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DependentInsuranceEligible"]) -> typing.Union[MetaOapg.properties.DependentInsuranceEligible, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DependentInsuranceEligibleDate"]) -> typing.Union[MetaOapg.properties.DependentInsuranceEligibleDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ApplicableBirthyear"]) -> typing.Union[MetaOapg.properties.ApplicableBirthyear, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Amount"]) -> typing.Union[MetaOapg.properties.Amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Percentage"]) -> typing.Union[MetaOapg.properties.Percentage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["NCCICode"]) -> typing.Union[MetaOapg.properties.NCCICode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PsdCode"]) -> typing.Union[MetaOapg.properties.PsdCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PsdRate"]) -> typing.Union[MetaOapg.properties.PsdRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OnHold"]) -> typing.Union[MetaOapg.properties.OnHold, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Exemptions"]) -> typing.Union['EmployeeExemptions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TaxCredit"]) -> typing.Union['EmployeeTaxCredit', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Id", "LegalEntityTaxId", "ReciprocityType", "FilingStatus", "WithholdingEffectiveStartDate", "BlockDate", "NonResidentAlien", "IsProbationaryEmployee", "OccupationalCode", "GeographicCode", "SOCCode", "SeasonalCode", "CountyCode", "SpouseWork", "DependentInsuranceEligible", "DependentInsuranceEligibleDate", "ApplicableBirthyear", "Amount", "Percentage", "NCCICode", "PsdCode", "PsdRate", "OnHold", "Exemptions", "TaxCredit", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        LegalEntityTaxId: typing.Union[MetaOapg.properties.LegalEntityTaxId, str, ],
        Id: typing.Union[MetaOapg.properties.Id, str, ],
        ReciprocityType: typing.Union['ReciprocityType', schemas.Unset] = schemas.unset,
        FilingStatus: typing.Union['FilingStatus2', schemas.Unset] = schemas.unset,
        WithholdingEffectiveStartDate: typing.Union[MetaOapg.properties.WithholdingEffectiveStartDate, None, str, datetime, schemas.Unset] = schemas.unset,
        BlockDate: typing.Union[MetaOapg.properties.BlockDate, None, str, datetime, schemas.Unset] = schemas.unset,
        NonResidentAlien: typing.Union[MetaOapg.properties.NonResidentAlien, None, str, schemas.Unset] = schemas.unset,
        IsProbationaryEmployee: typing.Union[MetaOapg.properties.IsProbationaryEmployee, None, bool, schemas.Unset] = schemas.unset,
        OccupationalCode: typing.Union[MetaOapg.properties.OccupationalCode, None, str, schemas.Unset] = schemas.unset,
        GeographicCode: typing.Union[MetaOapg.properties.GeographicCode, None, str, schemas.Unset] = schemas.unset,
        SOCCode: typing.Union[MetaOapg.properties.SOCCode, None, str, schemas.Unset] = schemas.unset,
        SeasonalCode: typing.Union[MetaOapg.properties.SeasonalCode, None, str, schemas.Unset] = schemas.unset,
        CountyCode: typing.Union[MetaOapg.properties.CountyCode, None, str, schemas.Unset] = schemas.unset,
        SpouseWork: typing.Union[MetaOapg.properties.SpouseWork, None, str, schemas.Unset] = schemas.unset,
        DependentInsuranceEligible: typing.Union[MetaOapg.properties.DependentInsuranceEligible, None, str, schemas.Unset] = schemas.unset,
        DependentInsuranceEligibleDate: typing.Union[MetaOapg.properties.DependentInsuranceEligibleDate, None, str, datetime, schemas.Unset] = schemas.unset,
        ApplicableBirthyear: typing.Union[MetaOapg.properties.ApplicableBirthyear, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Amount: typing.Union[MetaOapg.properties.Amount, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        Percentage: typing.Union[MetaOapg.properties.Percentage, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        NCCICode: typing.Union[MetaOapg.properties.NCCICode, None, str, schemas.Unset] = schemas.unset,
        PsdCode: typing.Union[MetaOapg.properties.PsdCode, None, str, schemas.Unset] = schemas.unset,
        PsdRate: typing.Union[MetaOapg.properties.PsdRate, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        OnHold: typing.Union[MetaOapg.properties.OnHold, None, bool, schemas.Unset] = schemas.unset,
        Exemptions: typing.Union['EmployeeExemptions', schemas.Unset] = schemas.unset,
        TaxCredit: typing.Union['EmployeeTaxCredit', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeeTax3':
        return super().__new__(
            cls,
            *args,
            LegalEntityTaxId=LegalEntityTaxId,
            Id=Id,
            ReciprocityType=ReciprocityType,
            FilingStatus=FilingStatus,
            WithholdingEffectiveStartDate=WithholdingEffectiveStartDate,
            BlockDate=BlockDate,
            NonResidentAlien=NonResidentAlien,
            IsProbationaryEmployee=IsProbationaryEmployee,
            OccupationalCode=OccupationalCode,
            GeographicCode=GeographicCode,
            SOCCode=SOCCode,
            SeasonalCode=SeasonalCode,
            CountyCode=CountyCode,
            SpouseWork=SpouseWork,
            DependentInsuranceEligible=DependentInsuranceEligible,
            DependentInsuranceEligibleDate=DependentInsuranceEligibleDate,
            ApplicableBirthyear=ApplicableBirthyear,
            Amount=Amount,
            Percentage=Percentage,
            NCCICode=NCCICode,
            PsdCode=PsdCode,
            PsdRate=PsdRate,
            OnHold=OnHold,
            Exemptions=Exemptions,
            TaxCredit=TaxCredit,
            _configuration=_configuration,
            **kwargs,
        )

from paycor_python_sdk.model.employee_exemptions import EmployeeExemptions
from paycor_python_sdk.model.employee_tax_credit import EmployeeTaxCredit
from paycor_python_sdk.model.filing_status2 import FilingStatus2
from paycor_python_sdk.model.reciprocity_type import ReciprocityType
