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


class Employee(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The Employee model represents all Employee related information.
 Provides links to the Employee's associated Person, Legal Entity, Department, Earning, Deduction, Tax, Direct Deposit, Pay Rat and Custom Field information.
    """


    class MetaOapg:
        
        class properties:
            Id = schemas.StrSchema
            
            
            class EmployeeNumber(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'EmployeeNumber':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class AlternateEmployeeNumber(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'AlternateEmployeeNumber':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class BadgeNumber(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'BadgeNumber':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class FirstName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'FirstName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class MiddleName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'MiddleName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class LastName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'LastName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def Email() -> typing.Type['Email']:
                return Email
        
            @staticmethod
            def EmploymentDateData() -> typing.Type['EmploymentDateData']:
                return EmploymentDateData
        
            @staticmethod
            def PositionData() -> typing.Type['EmployeePositionData']:
                return EmployeePositionData
        
            @staticmethod
            def StatusData() -> typing.Type['EmployeeStatusData']:
                return EmployeeStatusData
        
            @staticmethod
            def WorkLocation() -> typing.Type['EmployeeWorkLocationData']:
                return EmployeeWorkLocationData
        
            @staticmethod
            def Earnings() -> typing.Type['ResourceReference']:
                return ResourceReference
        
            @staticmethod
            def Deductions() -> typing.Type['ResourceReference']:
                return ResourceReference
        
            @staticmethod
            def Taxes() -> typing.Type['ResourceReference']:
                return ResourceReference
        
            @staticmethod
            def DirectDeposits() -> typing.Type['ResourceReference']:
                return ResourceReference
        
            @staticmethod
            def PayRates() -> typing.Type['ResourceReference']:
                return ResourceReference
        
            @staticmethod
            def LegalEntity() -> typing.Type['ResourceReference']:
                return ResourceReference
        
            @staticmethod
            def Person() -> typing.Type['ResourceReference']:
                return ResourceReference
        
            @staticmethod
            def Department() -> typing.Type['ResourceReference']:
                return ResourceReference
            __annotations__ = {
                "Id": Id,
                "EmployeeNumber": EmployeeNumber,
                "AlternateEmployeeNumber": AlternateEmployeeNumber,
                "BadgeNumber": BadgeNumber,
                "FirstName": FirstName,
                "MiddleName": MiddleName,
                "LastName": LastName,
                "Email": Email,
                "EmploymentDateData": EmploymentDateData,
                "PositionData": PositionData,
                "StatusData": StatusData,
                "WorkLocation": WorkLocation,
                "Earnings": Earnings,
                "Deductions": Deductions,
                "Taxes": Taxes,
                "DirectDeposits": DirectDeposits,
                "PayRates": PayRates,
                "LegalEntity": LegalEntity,
                "Person": Person,
                "Department": Department,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Id"]) -> MetaOapg.properties.Id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EmployeeNumber"]) -> MetaOapg.properties.EmployeeNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AlternateEmployeeNumber"]) -> MetaOapg.properties.AlternateEmployeeNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BadgeNumber"]) -> MetaOapg.properties.BadgeNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FirstName"]) -> MetaOapg.properties.FirstName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MiddleName"]) -> MetaOapg.properties.MiddleName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LastName"]) -> MetaOapg.properties.LastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Email"]) -> 'Email': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EmploymentDateData"]) -> 'EmploymentDateData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PositionData"]) -> 'EmployeePositionData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StatusData"]) -> 'EmployeeStatusData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["WorkLocation"]) -> 'EmployeeWorkLocationData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Earnings"]) -> 'ResourceReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Deductions"]) -> 'ResourceReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Taxes"]) -> 'ResourceReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DirectDeposits"]) -> 'ResourceReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PayRates"]) -> 'ResourceReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LegalEntity"]) -> 'ResourceReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Person"]) -> 'ResourceReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Department"]) -> 'ResourceReference': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Id", "EmployeeNumber", "AlternateEmployeeNumber", "BadgeNumber", "FirstName", "MiddleName", "LastName", "Email", "EmploymentDateData", "PositionData", "StatusData", "WorkLocation", "Earnings", "Deductions", "Taxes", "DirectDeposits", "PayRates", "LegalEntity", "Person", "Department", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Id"]) -> typing.Union[MetaOapg.properties.Id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EmployeeNumber"]) -> typing.Union[MetaOapg.properties.EmployeeNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AlternateEmployeeNumber"]) -> typing.Union[MetaOapg.properties.AlternateEmployeeNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BadgeNumber"]) -> typing.Union[MetaOapg.properties.BadgeNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FirstName"]) -> typing.Union[MetaOapg.properties.FirstName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MiddleName"]) -> typing.Union[MetaOapg.properties.MiddleName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LastName"]) -> typing.Union[MetaOapg.properties.LastName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Email"]) -> typing.Union['Email', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EmploymentDateData"]) -> typing.Union['EmploymentDateData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PositionData"]) -> typing.Union['EmployeePositionData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StatusData"]) -> typing.Union['EmployeeStatusData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["WorkLocation"]) -> typing.Union['EmployeeWorkLocationData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Earnings"]) -> typing.Union['ResourceReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Deductions"]) -> typing.Union['ResourceReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Taxes"]) -> typing.Union['ResourceReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DirectDeposits"]) -> typing.Union['ResourceReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PayRates"]) -> typing.Union['ResourceReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LegalEntity"]) -> typing.Union['ResourceReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Person"]) -> typing.Union['ResourceReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Department"]) -> typing.Union['ResourceReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Id", "EmployeeNumber", "AlternateEmployeeNumber", "BadgeNumber", "FirstName", "MiddleName", "LastName", "Email", "EmploymentDateData", "PositionData", "StatusData", "WorkLocation", "Earnings", "Deductions", "Taxes", "DirectDeposits", "PayRates", "LegalEntity", "Person", "Department", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Id: typing.Union[MetaOapg.properties.Id, str, schemas.Unset] = schemas.unset,
        EmployeeNumber: typing.Union[MetaOapg.properties.EmployeeNumber, None, str, schemas.Unset] = schemas.unset,
        AlternateEmployeeNumber: typing.Union[MetaOapg.properties.AlternateEmployeeNumber, None, str, schemas.Unset] = schemas.unset,
        BadgeNumber: typing.Union[MetaOapg.properties.BadgeNumber, None, str, schemas.Unset] = schemas.unset,
        FirstName: typing.Union[MetaOapg.properties.FirstName, None, str, schemas.Unset] = schemas.unset,
        MiddleName: typing.Union[MetaOapg.properties.MiddleName, None, str, schemas.Unset] = schemas.unset,
        LastName: typing.Union[MetaOapg.properties.LastName, None, str, schemas.Unset] = schemas.unset,
        Email: typing.Union['Email', schemas.Unset] = schemas.unset,
        EmploymentDateData: typing.Union['EmploymentDateData', schemas.Unset] = schemas.unset,
        PositionData: typing.Union['EmployeePositionData', schemas.Unset] = schemas.unset,
        StatusData: typing.Union['EmployeeStatusData', schemas.Unset] = schemas.unset,
        WorkLocation: typing.Union['EmployeeWorkLocationData', schemas.Unset] = schemas.unset,
        Earnings: typing.Union['ResourceReference', schemas.Unset] = schemas.unset,
        Deductions: typing.Union['ResourceReference', schemas.Unset] = schemas.unset,
        Taxes: typing.Union['ResourceReference', schemas.Unset] = schemas.unset,
        DirectDeposits: typing.Union['ResourceReference', schemas.Unset] = schemas.unset,
        PayRates: typing.Union['ResourceReference', schemas.Unset] = schemas.unset,
        LegalEntity: typing.Union['ResourceReference', schemas.Unset] = schemas.unset,
        Person: typing.Union['ResourceReference', schemas.Unset] = schemas.unset,
        Department: typing.Union['ResourceReference', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Employee':
        return super().__new__(
            cls,
            *args,
            Id=Id,
            EmployeeNumber=EmployeeNumber,
            AlternateEmployeeNumber=AlternateEmployeeNumber,
            BadgeNumber=BadgeNumber,
            FirstName=FirstName,
            MiddleName=MiddleName,
            LastName=LastName,
            Email=Email,
            EmploymentDateData=EmploymentDateData,
            PositionData=PositionData,
            StatusData=StatusData,
            WorkLocation=WorkLocation,
            Earnings=Earnings,
            Deductions=Deductions,
            Taxes=Taxes,
            DirectDeposits=DirectDeposits,
            PayRates=PayRates,
            LegalEntity=LegalEntity,
            Person=Person,
            Department=Department,
            _configuration=_configuration,
            **kwargs,
        )

from paycor_python_sdk.model.email import Email
from paycor_python_sdk.model.employee_position_data import EmployeePositionData
from paycor_python_sdk.model.employee_status_data import EmployeeStatusData
from paycor_python_sdk.model.employee_work_location_data import EmployeeWorkLocationData
from paycor_python_sdk.model.employment_date_data import EmploymentDateData
from paycor_python_sdk.model.resource_reference import ResourceReference
