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


class Services(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The Services model represents service offerings available to a Legal Entity.
    """


    class MetaOapg:
        
        class properties:
            
            
            class TimeService(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'TimeService':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            TimeOnDemand = schemas.BoolSchema
            PerformTime = schemas.BoolSchema
            PerformTimeScheduling = schemas.BoolSchema
            PaycorScheduling = schemas.BoolSchema
            PaycorSchedulingPro = schemas.BoolSchema
            PerformAccruals = schemas.BoolSchema
            ResellerAccruals = schemas.BoolSchema
            PerformTimeOff = schemas.BoolSchema
            IntegrationPayrollTimePartner = schemas.BoolSchema
            WorkforceManagement = schemas.BoolSchema
            JobCosting = schemas.BoolSchema
            Onboarding = schemas.BoolSchema
            __annotations__ = {
                "TimeService": TimeService,
                "TimeOnDemand": TimeOnDemand,
                "PerformTime": PerformTime,
                "PerformTimeScheduling": PerformTimeScheduling,
                "PaycorScheduling": PaycorScheduling,
                "PaycorSchedulingPro": PaycorSchedulingPro,
                "PerformAccruals": PerformAccruals,
                "ResellerAccruals": ResellerAccruals,
                "PerformTimeOff": PerformTimeOff,
                "IntegrationPayrollTimePartner": IntegrationPayrollTimePartner,
                "WorkforceManagement": WorkforceManagement,
                "JobCosting": JobCosting,
                "Onboarding": Onboarding,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeService"]) -> MetaOapg.properties.TimeService: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimeOnDemand"]) -> MetaOapg.properties.TimeOnDemand: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PerformTime"]) -> MetaOapg.properties.PerformTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PerformTimeScheduling"]) -> MetaOapg.properties.PerformTimeScheduling: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PaycorScheduling"]) -> MetaOapg.properties.PaycorScheduling: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PaycorSchedulingPro"]) -> MetaOapg.properties.PaycorSchedulingPro: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PerformAccruals"]) -> MetaOapg.properties.PerformAccruals: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ResellerAccruals"]) -> MetaOapg.properties.ResellerAccruals: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PerformTimeOff"]) -> MetaOapg.properties.PerformTimeOff: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IntegrationPayrollTimePartner"]) -> MetaOapg.properties.IntegrationPayrollTimePartner: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["WorkforceManagement"]) -> MetaOapg.properties.WorkforceManagement: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["JobCosting"]) -> MetaOapg.properties.JobCosting: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Onboarding"]) -> MetaOapg.properties.Onboarding: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["TimeService", "TimeOnDemand", "PerformTime", "PerformTimeScheduling", "PaycorScheduling", "PaycorSchedulingPro", "PerformAccruals", "ResellerAccruals", "PerformTimeOff", "IntegrationPayrollTimePartner", "WorkforceManagement", "JobCosting", "Onboarding", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeService"]) -> typing.Union[MetaOapg.properties.TimeService, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimeOnDemand"]) -> typing.Union[MetaOapg.properties.TimeOnDemand, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PerformTime"]) -> typing.Union[MetaOapg.properties.PerformTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PerformTimeScheduling"]) -> typing.Union[MetaOapg.properties.PerformTimeScheduling, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PaycorScheduling"]) -> typing.Union[MetaOapg.properties.PaycorScheduling, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PaycorSchedulingPro"]) -> typing.Union[MetaOapg.properties.PaycorSchedulingPro, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PerformAccruals"]) -> typing.Union[MetaOapg.properties.PerformAccruals, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ResellerAccruals"]) -> typing.Union[MetaOapg.properties.ResellerAccruals, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PerformTimeOff"]) -> typing.Union[MetaOapg.properties.PerformTimeOff, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IntegrationPayrollTimePartner"]) -> typing.Union[MetaOapg.properties.IntegrationPayrollTimePartner, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["WorkforceManagement"]) -> typing.Union[MetaOapg.properties.WorkforceManagement, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["JobCosting"]) -> typing.Union[MetaOapg.properties.JobCosting, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Onboarding"]) -> typing.Union[MetaOapg.properties.Onboarding, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["TimeService", "TimeOnDemand", "PerformTime", "PerformTimeScheduling", "PaycorScheduling", "PaycorSchedulingPro", "PerformAccruals", "ResellerAccruals", "PerformTimeOff", "IntegrationPayrollTimePartner", "WorkforceManagement", "JobCosting", "Onboarding", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        TimeService: typing.Union[MetaOapg.properties.TimeService, None, str, schemas.Unset] = schemas.unset,
        TimeOnDemand: typing.Union[MetaOapg.properties.TimeOnDemand, bool, schemas.Unset] = schemas.unset,
        PerformTime: typing.Union[MetaOapg.properties.PerformTime, bool, schemas.Unset] = schemas.unset,
        PerformTimeScheduling: typing.Union[MetaOapg.properties.PerformTimeScheduling, bool, schemas.Unset] = schemas.unset,
        PaycorScheduling: typing.Union[MetaOapg.properties.PaycorScheduling, bool, schemas.Unset] = schemas.unset,
        PaycorSchedulingPro: typing.Union[MetaOapg.properties.PaycorSchedulingPro, bool, schemas.Unset] = schemas.unset,
        PerformAccruals: typing.Union[MetaOapg.properties.PerformAccruals, bool, schemas.Unset] = schemas.unset,
        ResellerAccruals: typing.Union[MetaOapg.properties.ResellerAccruals, bool, schemas.Unset] = schemas.unset,
        PerformTimeOff: typing.Union[MetaOapg.properties.PerformTimeOff, bool, schemas.Unset] = schemas.unset,
        IntegrationPayrollTimePartner: typing.Union[MetaOapg.properties.IntegrationPayrollTimePartner, bool, schemas.Unset] = schemas.unset,
        WorkforceManagement: typing.Union[MetaOapg.properties.WorkforceManagement, bool, schemas.Unset] = schemas.unset,
        JobCosting: typing.Union[MetaOapg.properties.JobCosting, bool, schemas.Unset] = schemas.unset,
        Onboarding: typing.Union[MetaOapg.properties.Onboarding, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Services':
        return super().__new__(
            cls,
            *args,
            TimeService=TimeService,
            TimeOnDemand=TimeOnDemand,
            PerformTime=PerformTime,
            PerformTimeScheduling=PerformTimeScheduling,
            PaycorScheduling=PaycorScheduling,
            PaycorSchedulingPro=PaycorSchedulingPro,
            PerformAccruals=PerformAccruals,
            ResellerAccruals=ResellerAccruals,
            PerformTimeOff=PerformTimeOff,
            IntegrationPayrollTimePartner=IntegrationPayrollTimePartner,
            WorkforceManagement=WorkforceManagement,
            JobCosting=JobCosting,
            Onboarding=Onboarding,
            _configuration=_configuration,
            **kwargs,
        )
