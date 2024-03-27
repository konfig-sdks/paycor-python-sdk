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


class EmployeePositionAndStatus(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The PUT Employee Position And Status model allows updating Employee's Position and Status Information fields. 
Employee Status fields are: EmploymentStatus and RehireDate. Both fields have to be set in order to update Employee Status.
Employee Position fields are: EmploymentType, WorkLocation, JobTitle, FLSA, ManagerId, DepartmentId. Fields EmployeeType and WorkLocation have to be set in order to update Employee Position.
    """


    class MetaOapg:
        required = {
            "RehireDate",
            "WorkLocation",
            "EmploymentStatus",
            "EmploymentType",
        }
        
        class properties:
        
            @staticmethod
            def EmploymentStatus() -> typing.Type['EmploymentStatus2']:
                return EmploymentStatus2
            
            
            class RehireDate(
                schemas.DateTimeSchema
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
                    min_length = 1
        
            @staticmethod
            def EmploymentType() -> typing.Type['EmploymentType']:
                return EmploymentType
            
            
            class WorkLocation(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 1
            
            
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
        
            @staticmethod
            def Flsa() -> typing.Type['FlsaType']:
                return FlsaType
            
            
            class ManagerId(
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
                ) -> 'ManagerId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class DepartmentId(
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
                ) -> 'DepartmentId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "EmploymentStatus": EmploymentStatus,
                "RehireDate": RehireDate,
                "EmploymentType": EmploymentType,
                "WorkLocation": WorkLocation,
                "JobTitle": JobTitle,
                "Flsa": Flsa,
                "ManagerId": ManagerId,
                "DepartmentId": DepartmentId,
            }
    
    RehireDate: MetaOapg.properties.RehireDate
    WorkLocation: MetaOapg.properties.WorkLocation
    EmploymentStatus: 'EmploymentStatus2'
    EmploymentType: 'EmploymentType'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EmploymentStatus"]) -> 'EmploymentStatus2': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["RehireDate"]) -> MetaOapg.properties.RehireDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EmploymentType"]) -> 'EmploymentType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["WorkLocation"]) -> MetaOapg.properties.WorkLocation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["JobTitle"]) -> MetaOapg.properties.JobTitle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Flsa"]) -> 'FlsaType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ManagerId"]) -> MetaOapg.properties.ManagerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DepartmentId"]) -> MetaOapg.properties.DepartmentId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["EmploymentStatus", "RehireDate", "EmploymentType", "WorkLocation", "JobTitle", "Flsa", "ManagerId", "DepartmentId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EmploymentStatus"]) -> 'EmploymentStatus2': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["RehireDate"]) -> MetaOapg.properties.RehireDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EmploymentType"]) -> 'EmploymentType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["WorkLocation"]) -> MetaOapg.properties.WorkLocation: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["JobTitle"]) -> typing.Union[MetaOapg.properties.JobTitle, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Flsa"]) -> typing.Union['FlsaType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ManagerId"]) -> typing.Union[MetaOapg.properties.ManagerId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DepartmentId"]) -> typing.Union[MetaOapg.properties.DepartmentId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["EmploymentStatus", "RehireDate", "EmploymentType", "WorkLocation", "JobTitle", "Flsa", "ManagerId", "DepartmentId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        RehireDate: typing.Union[MetaOapg.properties.RehireDate, str, datetime, ],
        WorkLocation: typing.Union[MetaOapg.properties.WorkLocation, str, ],
        EmploymentStatus: 'EmploymentStatus2',
        EmploymentType: 'EmploymentType',
        JobTitle: typing.Union[MetaOapg.properties.JobTitle, None, str, schemas.Unset] = schemas.unset,
        Flsa: typing.Union['FlsaType', schemas.Unset] = schemas.unset,
        ManagerId: typing.Union[MetaOapg.properties.ManagerId, None, str, schemas.Unset] = schemas.unset,
        DepartmentId: typing.Union[MetaOapg.properties.DepartmentId, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeePositionAndStatus':
        return super().__new__(
            cls,
            *args,
            RehireDate=RehireDate,
            WorkLocation=WorkLocation,
            EmploymentStatus=EmploymentStatus,
            EmploymentType=EmploymentType,
            JobTitle=JobTitle,
            Flsa=Flsa,
            ManagerId=ManagerId,
            DepartmentId=DepartmentId,
            _configuration=_configuration,
            **kwargs,
        )

from paycor_python_sdk.model.employment_status2 import EmploymentStatus2
from paycor_python_sdk.model.employment_type import EmploymentType
from paycor_python_sdk.model.flsa_type import FlsaType
