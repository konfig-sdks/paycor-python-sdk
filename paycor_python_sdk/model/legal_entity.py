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


class LegalEntity(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The Legal Entity (Client) model represents organization Legal Entity information.
Provides links to the Legal Entity's associated Tenant, Employee, Person, Earning, Deduction, Taxes and Custom Field information.
    """


    class MetaOapg:
        
        class properties:
            Id = schemas.Int32Schema
            
            
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
            
            
            class FederalId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'FederalId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def Type() -> typing.Type['CorporationType']:
                return CorporationType
            IsLost = schemas.BoolSchema
            
            
            class BusinessNames(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['BusinessName']:
                        return BusinessName
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'BusinessNames':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def Tenant() -> typing.Type['ResourceReference']:
                return ResourceReference
        
            @staticmethod
            def Employees() -> typing.Type['ResourceReference']:
                return ResourceReference
        
            @staticmethod
            def Persons() -> typing.Type['ResourceReference']:
                return ResourceReference
        
            @staticmethod
            def Earnings() -> typing.Type['ResourceReference']:
                return ResourceReference
        
            @staticmethod
            def Deductions() -> typing.Type['ResourceReference']:
                return ResourceReference
        
            @staticmethod
            def Taxes() -> typing.Type['ResourceReference']:
                return ResourceReference
            __annotations__ = {
                "Id": Id,
                "Name": Name,
                "FederalId": FederalId,
                "Type": Type,
                "IsLost": IsLost,
                "BusinessNames": BusinessNames,
                "Tenant": Tenant,
                "Employees": Employees,
                "Persons": Persons,
                "Earnings": Earnings,
                "Deductions": Deductions,
                "Taxes": Taxes,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Id"]) -> MetaOapg.properties.Id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Name"]) -> MetaOapg.properties.Name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FederalId"]) -> MetaOapg.properties.FederalId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Type"]) -> 'CorporationType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IsLost"]) -> MetaOapg.properties.IsLost: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BusinessNames"]) -> MetaOapg.properties.BusinessNames: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Tenant"]) -> 'ResourceReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Employees"]) -> 'ResourceReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Persons"]) -> 'ResourceReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Earnings"]) -> 'ResourceReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Deductions"]) -> 'ResourceReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Taxes"]) -> 'ResourceReference': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Id", "Name", "FederalId", "Type", "IsLost", "BusinessNames", "Tenant", "Employees", "Persons", "Earnings", "Deductions", "Taxes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Id"]) -> typing.Union[MetaOapg.properties.Id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Name"]) -> typing.Union[MetaOapg.properties.Name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FederalId"]) -> typing.Union[MetaOapg.properties.FederalId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Type"]) -> typing.Union['CorporationType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IsLost"]) -> typing.Union[MetaOapg.properties.IsLost, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BusinessNames"]) -> typing.Union[MetaOapg.properties.BusinessNames, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Tenant"]) -> typing.Union['ResourceReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Employees"]) -> typing.Union['ResourceReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Persons"]) -> typing.Union['ResourceReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Earnings"]) -> typing.Union['ResourceReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Deductions"]) -> typing.Union['ResourceReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Taxes"]) -> typing.Union['ResourceReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Id", "Name", "FederalId", "Type", "IsLost", "BusinessNames", "Tenant", "Employees", "Persons", "Earnings", "Deductions", "Taxes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Id: typing.Union[MetaOapg.properties.Id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Name: typing.Union[MetaOapg.properties.Name, None, str, schemas.Unset] = schemas.unset,
        FederalId: typing.Union[MetaOapg.properties.FederalId, None, str, schemas.Unset] = schemas.unset,
        Type: typing.Union['CorporationType', schemas.Unset] = schemas.unset,
        IsLost: typing.Union[MetaOapg.properties.IsLost, bool, schemas.Unset] = schemas.unset,
        BusinessNames: typing.Union[MetaOapg.properties.BusinessNames, list, tuple, None, schemas.Unset] = schemas.unset,
        Tenant: typing.Union['ResourceReference', schemas.Unset] = schemas.unset,
        Employees: typing.Union['ResourceReference', schemas.Unset] = schemas.unset,
        Persons: typing.Union['ResourceReference', schemas.Unset] = schemas.unset,
        Earnings: typing.Union['ResourceReference', schemas.Unset] = schemas.unset,
        Deductions: typing.Union['ResourceReference', schemas.Unset] = schemas.unset,
        Taxes: typing.Union['ResourceReference', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LegalEntity':
        return super().__new__(
            cls,
            *args,
            Id=Id,
            Name=Name,
            FederalId=FederalId,
            Type=Type,
            IsLost=IsLost,
            BusinessNames=BusinessNames,
            Tenant=Tenant,
            Employees=Employees,
            Persons=Persons,
            Earnings=Earnings,
            Deductions=Deductions,
            Taxes=Taxes,
            _configuration=_configuration,
            **kwargs,
        )

from paycor_python_sdk.model.business_name import BusinessName
from paycor_python_sdk.model.corporation_type import CorporationType
from paycor_python_sdk.model.resource_reference import ResourceReference
