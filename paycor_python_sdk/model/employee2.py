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


class Employee2(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The Create Employee model represents Employee related information needed to create a new employee (a new hire).
    """


    class MetaOapg:
        required = {
            "DepartmentCode",
            "Status",
            "PrimaryAddress",
            "FirstName",
            "LegalEntityId",
            "HireDate",
            "LastName",
            "PaygroupDescription",
        }
        
        class properties:
            LegalEntityId = schemas.Int32Schema
            
            
            class FirstName(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 1
            
            
            class LastName(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 1
            
            
            class HireDate(
                schemas.DateTimeSchema
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
                    min_length = 1
        
            @staticmethod
            def Status() -> typing.Type['EmploymentStatus']:
                return EmploymentStatus
            
            
            class PaygroupDescription(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 1
            DepartmentCode = schemas.Int64Schema
        
            @staticmethod
            def PrimaryAddress() -> typing.Type['GenericAddress']:
                return GenericAddress
            
            
            class EmployeeNumber(
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
        
            @staticmethod
            def Prefix() -> typing.Type['Prefix']:
                return Prefix
            
            
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
        
            @staticmethod
            def Suffix() -> typing.Type['Suffix']:
                return Suffix
            
            
            class HomeEmail(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'HomeEmail':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class WorkEmail(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'WorkEmail':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class Phones(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Phone']:
                        return Phone
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Phones':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class SocialSecurityNumber(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'SocialSecurityNumber':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class BirthDate(
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
                ) -> 'BirthDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def Gender() -> typing.Type['Gender']:
                return Gender
        
            @staticmethod
            def Ethnicity() -> typing.Type['EthnicityType']:
                return EthnicityType
        
            @staticmethod
            def MaritalStatus() -> typing.Type['MaritalStatus']:
                return MaritalStatus
            
            
            class WorkLocation(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'WorkLocation':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class JobTitle(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'JobTitle':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class ReHireDate(
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
                ) -> 'ReHireDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def Flsa() -> typing.Type['FlsaType']:
                return FlsaType
        
            @staticmethod
            def Type() -> typing.Type['EmploymentType']:
                return EmploymentType
            
            
            class ManagerEmpId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'guid'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ManagerEmpId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def Veteran() -> typing.Type['VeteranStatus']:
                return VeteranStatus
        
            @staticmethod
            def Disability() -> typing.Type['DisabilityStatus']:
                return DisabilityStatus
            __annotations__ = {
                "LegalEntityId": LegalEntityId,
                "FirstName": FirstName,
                "LastName": LastName,
                "HireDate": HireDate,
                "Status": Status,
                "PaygroupDescription": PaygroupDescription,
                "DepartmentCode": DepartmentCode,
                "PrimaryAddress": PrimaryAddress,
                "EmployeeNumber": EmployeeNumber,
                "AlternateEmployeeNumber": AlternateEmployeeNumber,
                "Prefix": Prefix,
                "MiddleName": MiddleName,
                "Suffix": Suffix,
                "HomeEmail": HomeEmail,
                "WorkEmail": WorkEmail,
                "Phones": Phones,
                "SocialSecurityNumber": SocialSecurityNumber,
                "BirthDate": BirthDate,
                "Gender": Gender,
                "Ethnicity": Ethnicity,
                "MaritalStatus": MaritalStatus,
                "WorkLocation": WorkLocation,
                "JobTitle": JobTitle,
                "ReHireDate": ReHireDate,
                "Flsa": Flsa,
                "Type": Type,
                "ManagerEmpId": ManagerEmpId,
                "Veteran": Veteran,
                "Disability": Disability,
            }
    
    DepartmentCode: MetaOapg.properties.DepartmentCode
    Status: 'EmploymentStatus'
    PrimaryAddress: 'GenericAddress'
    FirstName: MetaOapg.properties.FirstName
    LegalEntityId: MetaOapg.properties.LegalEntityId
    HireDate: MetaOapg.properties.HireDate
    LastName: MetaOapg.properties.LastName
    PaygroupDescription: MetaOapg.properties.PaygroupDescription
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LegalEntityId"]) -> MetaOapg.properties.LegalEntityId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FirstName"]) -> MetaOapg.properties.FirstName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LastName"]) -> MetaOapg.properties.LastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["HireDate"]) -> MetaOapg.properties.HireDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Status"]) -> 'EmploymentStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PaygroupDescription"]) -> MetaOapg.properties.PaygroupDescription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DepartmentCode"]) -> MetaOapg.properties.DepartmentCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PrimaryAddress"]) -> 'GenericAddress': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EmployeeNumber"]) -> MetaOapg.properties.EmployeeNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AlternateEmployeeNumber"]) -> MetaOapg.properties.AlternateEmployeeNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Prefix"]) -> 'Prefix': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MiddleName"]) -> MetaOapg.properties.MiddleName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Suffix"]) -> 'Suffix': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["HomeEmail"]) -> MetaOapg.properties.HomeEmail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["WorkEmail"]) -> MetaOapg.properties.WorkEmail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Phones"]) -> MetaOapg.properties.Phones: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SocialSecurityNumber"]) -> MetaOapg.properties.SocialSecurityNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BirthDate"]) -> MetaOapg.properties.BirthDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Gender"]) -> 'Gender': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Ethnicity"]) -> 'EthnicityType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MaritalStatus"]) -> 'MaritalStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["WorkLocation"]) -> MetaOapg.properties.WorkLocation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["JobTitle"]) -> MetaOapg.properties.JobTitle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ReHireDate"]) -> MetaOapg.properties.ReHireDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Flsa"]) -> 'FlsaType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Type"]) -> 'EmploymentType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ManagerEmpId"]) -> MetaOapg.properties.ManagerEmpId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Veteran"]) -> 'VeteranStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Disability"]) -> 'DisabilityStatus': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["LegalEntityId", "FirstName", "LastName", "HireDate", "Status", "PaygroupDescription", "DepartmentCode", "PrimaryAddress", "EmployeeNumber", "AlternateEmployeeNumber", "Prefix", "MiddleName", "Suffix", "HomeEmail", "WorkEmail", "Phones", "SocialSecurityNumber", "BirthDate", "Gender", "Ethnicity", "MaritalStatus", "WorkLocation", "JobTitle", "ReHireDate", "Flsa", "Type", "ManagerEmpId", "Veteran", "Disability", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LegalEntityId"]) -> MetaOapg.properties.LegalEntityId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FirstName"]) -> MetaOapg.properties.FirstName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LastName"]) -> MetaOapg.properties.LastName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["HireDate"]) -> MetaOapg.properties.HireDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Status"]) -> 'EmploymentStatus': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PaygroupDescription"]) -> MetaOapg.properties.PaygroupDescription: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DepartmentCode"]) -> MetaOapg.properties.DepartmentCode: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PrimaryAddress"]) -> 'GenericAddress': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EmployeeNumber"]) -> typing.Union[MetaOapg.properties.EmployeeNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AlternateEmployeeNumber"]) -> typing.Union[MetaOapg.properties.AlternateEmployeeNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Prefix"]) -> typing.Union['Prefix', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MiddleName"]) -> typing.Union[MetaOapg.properties.MiddleName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Suffix"]) -> typing.Union['Suffix', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["HomeEmail"]) -> typing.Union[MetaOapg.properties.HomeEmail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["WorkEmail"]) -> typing.Union[MetaOapg.properties.WorkEmail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Phones"]) -> typing.Union[MetaOapg.properties.Phones, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SocialSecurityNumber"]) -> typing.Union[MetaOapg.properties.SocialSecurityNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BirthDate"]) -> typing.Union[MetaOapg.properties.BirthDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Gender"]) -> typing.Union['Gender', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Ethnicity"]) -> typing.Union['EthnicityType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MaritalStatus"]) -> typing.Union['MaritalStatus', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["WorkLocation"]) -> typing.Union[MetaOapg.properties.WorkLocation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["JobTitle"]) -> typing.Union[MetaOapg.properties.JobTitle, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ReHireDate"]) -> typing.Union[MetaOapg.properties.ReHireDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Flsa"]) -> typing.Union['FlsaType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Type"]) -> typing.Union['EmploymentType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ManagerEmpId"]) -> typing.Union[MetaOapg.properties.ManagerEmpId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Veteran"]) -> typing.Union['VeteranStatus', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Disability"]) -> typing.Union['DisabilityStatus', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["LegalEntityId", "FirstName", "LastName", "HireDate", "Status", "PaygroupDescription", "DepartmentCode", "PrimaryAddress", "EmployeeNumber", "AlternateEmployeeNumber", "Prefix", "MiddleName", "Suffix", "HomeEmail", "WorkEmail", "Phones", "SocialSecurityNumber", "BirthDate", "Gender", "Ethnicity", "MaritalStatus", "WorkLocation", "JobTitle", "ReHireDate", "Flsa", "Type", "ManagerEmpId", "Veteran", "Disability", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        DepartmentCode: typing.Union[MetaOapg.properties.DepartmentCode, decimal.Decimal, int, ],
        Status: 'EmploymentStatus',
        PrimaryAddress: 'GenericAddress',
        FirstName: typing.Union[MetaOapg.properties.FirstName, str, ],
        LegalEntityId: typing.Union[MetaOapg.properties.LegalEntityId, decimal.Decimal, int, ],
        HireDate: typing.Union[MetaOapg.properties.HireDate, str, datetime, ],
        LastName: typing.Union[MetaOapg.properties.LastName, str, ],
        PaygroupDescription: typing.Union[MetaOapg.properties.PaygroupDescription, str, ],
        EmployeeNumber: typing.Union[MetaOapg.properties.EmployeeNumber, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        AlternateEmployeeNumber: typing.Union[MetaOapg.properties.AlternateEmployeeNumber, None, str, schemas.Unset] = schemas.unset,
        Prefix: typing.Union['Prefix', schemas.Unset] = schemas.unset,
        MiddleName: typing.Union[MetaOapg.properties.MiddleName, None, str, schemas.Unset] = schemas.unset,
        Suffix: typing.Union['Suffix', schemas.Unset] = schemas.unset,
        HomeEmail: typing.Union[MetaOapg.properties.HomeEmail, None, str, schemas.Unset] = schemas.unset,
        WorkEmail: typing.Union[MetaOapg.properties.WorkEmail, None, str, schemas.Unset] = schemas.unset,
        Phones: typing.Union[MetaOapg.properties.Phones, list, tuple, None, schemas.Unset] = schemas.unset,
        SocialSecurityNumber: typing.Union[MetaOapg.properties.SocialSecurityNumber, None, str, schemas.Unset] = schemas.unset,
        BirthDate: typing.Union[MetaOapg.properties.BirthDate, None, str, datetime, schemas.Unset] = schemas.unset,
        Gender: typing.Union['Gender', schemas.Unset] = schemas.unset,
        Ethnicity: typing.Union['EthnicityType', schemas.Unset] = schemas.unset,
        MaritalStatus: typing.Union['MaritalStatus', schemas.Unset] = schemas.unset,
        WorkLocation: typing.Union[MetaOapg.properties.WorkLocation, None, str, schemas.Unset] = schemas.unset,
        JobTitle: typing.Union[MetaOapg.properties.JobTitle, None, str, schemas.Unset] = schemas.unset,
        ReHireDate: typing.Union[MetaOapg.properties.ReHireDate, None, str, datetime, schemas.Unset] = schemas.unset,
        Flsa: typing.Union['FlsaType', schemas.Unset] = schemas.unset,
        Type: typing.Union['EmploymentType', schemas.Unset] = schemas.unset,
        ManagerEmpId: typing.Union[MetaOapg.properties.ManagerEmpId, None, str, schemas.Unset] = schemas.unset,
        Veteran: typing.Union['VeteranStatus', schemas.Unset] = schemas.unset,
        Disability: typing.Union['DisabilityStatus', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Employee2':
        return super().__new__(
            cls,
            *args,
            DepartmentCode=DepartmentCode,
            Status=Status,
            PrimaryAddress=PrimaryAddress,
            FirstName=FirstName,
            LegalEntityId=LegalEntityId,
            HireDate=HireDate,
            LastName=LastName,
            PaygroupDescription=PaygroupDescription,
            EmployeeNumber=EmployeeNumber,
            AlternateEmployeeNumber=AlternateEmployeeNumber,
            Prefix=Prefix,
            MiddleName=MiddleName,
            Suffix=Suffix,
            HomeEmail=HomeEmail,
            WorkEmail=WorkEmail,
            Phones=Phones,
            SocialSecurityNumber=SocialSecurityNumber,
            BirthDate=BirthDate,
            Gender=Gender,
            Ethnicity=Ethnicity,
            MaritalStatus=MaritalStatus,
            WorkLocation=WorkLocation,
            JobTitle=JobTitle,
            ReHireDate=ReHireDate,
            Flsa=Flsa,
            Type=Type,
            ManagerEmpId=ManagerEmpId,
            Veteran=Veteran,
            Disability=Disability,
            _configuration=_configuration,
            **kwargs,
        )

from paycor_python_sdk.model.disability_status import DisabilityStatus
from paycor_python_sdk.model.employment_status import EmploymentStatus
from paycor_python_sdk.model.employment_type import EmploymentType
from paycor_python_sdk.model.ethnicity_type import EthnicityType
from paycor_python_sdk.model.flsa_type import FlsaType
from paycor_python_sdk.model.gender import Gender
from paycor_python_sdk.model.generic_address import GenericAddress
from paycor_python_sdk.model.marital_status import MaritalStatus
from paycor_python_sdk.model.phone import Phone
from paycor_python_sdk.model.prefix import Prefix
from paycor_python_sdk.model.suffix import Suffix
from paycor_python_sdk.model.veteran_status import VeteranStatus
