# coding: utf-8

"""
    Paycor Public API

     Welcome to Paycor's Public API! This document is a reference for the APIs Paycor has available, and acts as a complement to the \"Guides\" section.   # Getting Started  <strong>To learn more about getting started with Paycor's Public APIs, check out our <a href=\"/guides\">Guides.</a></strong>  # GET, PUT, POST  * When requesting object, use GET endpoints. All list endpoints support paging, as described [in the other doc].  * When creating an object, use POST endpoints. Your code will need to create an object and send it to Paycor in your API call request body as JSON. You can use the \"request sample\" body as a starting point. Our endpoints will return a reference to the created object (the ID and GET API URL) for your system. * When updating an object, you will use PUT endpoints. The general flow would be to: GET the object you want to update, modify the fields as desired, then PUT the object (as JSON in the request body) to our endpoints. Some fields like the object's ID cannot be updated because they are system-set.'   # Error Handling  * 400: Please consult the response text to correct your request information.  * 401 with response \"Access denied due to missing subscription key\": Please include your APIM Subscription Key as header Ocp-Apim-Subscription-Key or querystring parameter subscription-key.  * 401 with no response: Please ensure you included a valid & current Access Token in the Authorization header. * 403: Please ensure your Access Token's scope has all the relevant access you need, on the AppCreator Data Access screen.  * 404: Please validate the API route you are using. If that is correct, one of your IDs most likely does not exist or is not in a valid state.  * 429: Paycor implements rate limits for our Public API. Each customer (implemented via APIM subscription key) has a limited number of calls. The number of calls is counted across all APIs, not per individual API. Please use bulk endpoints where available and spread your calls over a wider timespan.   * The default rate limit is up to 1000 API calls per minute (total across all our Public APIs).  * 500: Please contact Paycor. When you make a POST or PUT call and receive a 500, please do not retry the call automatically - this may result in double-posting. GETs can be safely retried.   # IDs  * ClientId = LegalEntityId * TenantId = CompanyId * EmployeeId is not visible in Paycor's UI, you must retrieve it from the Public API  # Earnings, Deductions, Taxes  This section describes the domain model for Paycor's Earnings, Deductions, and Taxes. This will provide background for many paydata-related Public API endpoints.   Paycor stores Earnings, Deductions, and Taxes each at three levels: * Global: Same data across all legal entities. Setup by Paycor for customers to choose from. Sample Codes (note these will not be setup on every Legal Entity):   * Earnings: REG, OT   * Taxes: FITWH, SOC, SOCER, OHCIN   * Deductions: 401k, KMat, H125, UWay * Legal Entity or Tenant: Codes setup &amp; customized on the legal entity or Tenant level. Must be tied to a Global Code.    * Perform UI allows creating Deduction and Earning codes on Tenant level (under Configure Company nav menu). These will be returned by the Legal Entity Public API endpoints.  * Employee: codes setup on a particular employee, tied to a Legal Entity-level or Tenant-level code   * Employee Earnings/Deductions/Taxes are applied during payroll. Many properties are inherited from the Legal Entity or Global levels, but some can be overridden.   # Authentication  <!-- ReDoc-Inject: <security-definitions> -->

    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from paycor_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from paycor_python_sdk.api_response import AsyncGeneratorResponse
from paycor_python_sdk import api_client, exceptions
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

from paycor_python_sdk.model.includes14 import Includes14 as Includes14Schema
from paycor_python_sdk.model.email_type_options2 import EmailTypeOptions2 as EmailTypeOptions2Schema
from paycor_python_sdk.model.paycor_error import PaycorError as PaycorErrorSchema
from paycor_python_sdk.model.paged_result_of_employee_return_item import PagedResultOfEmployeeReturnItem as PagedResultOfEmployeeReturnItemSchema
from paycor_python_sdk.model.employment_status import EmploymentStatus as EmploymentStatusSchema

from paycor_python_sdk.type.email_type_options2 import EmailTypeOptions2
from paycor_python_sdk.type.employment_status import EmploymentStatus
from paycor_python_sdk.type.paged_result_of_employee_return_item import PagedResultOfEmployeeReturnItem
from paycor_python_sdk.type.paycor_error import PaycorError
from paycor_python_sdk.type.includes14 import Includes14

from ...api_client import Dictionary
from paycor_python_sdk.pydantic.paged_result_of_employee_return_item import PagedResultOfEmployeeReturnItem as PagedResultOfEmployeeReturnItemPydantic
from paycor_python_sdk.pydantic.employment_status import EmploymentStatus as EmploymentStatusPydantic
from paycor_python_sdk.pydantic.includes14 import Includes14 as Includes14Pydantic
from paycor_python_sdk.pydantic.email_type_options2 import EmailTypeOptions2 as EmailTypeOptions2Pydantic
from paycor_python_sdk.pydantic.paycor_error import PaycorError as PaycorErrorPydantic

# Query params


class IncludeSchema(
    schemas.ListBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneTupleMixin
):


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['Includes14']:
            return Includes14


    def __new__(
        cls,
        *args: typing.Union[list, tuple, None, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'IncludeSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )
EmailTypeSchema = EmailTypeOptions2Schema
StatusFilterSchema = EmploymentStatusSchema


class EmployeeNumberSchema(
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
    ) -> 'EmployeeNumberSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )


class LastNameSchema(
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):


    def __new__(
        cls,
        *args: typing.Union[None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'LastNameSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )


class DepartmentCodeSchema(
    schemas.Int64Base,
    schemas.IntBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneDecimalMixin
):


    class MetaOapg:
        format = 'int64'


    def __new__(
        cls,
        *args: typing.Union[None, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'DepartmentCodeSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )


class WorkLocationNameSchema(
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):


    def __new__(
        cls,
        *args: typing.Union[None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'WorkLocationNameSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )


class ContinuationTokenSchema(
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
    ) -> 'ContinuationTokenSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'include': typing.Union[IncludeSchema, list, tuple, None, ],
        'emailType': typing.Union[EmailTypeSchema, ],
        'statusFilter': typing.Union[StatusFilterSchema, ],
        'employeeNumber': typing.Union[EmployeeNumberSchema, None, decimal.Decimal, int, ],
        'lastName': typing.Union[LastNameSchema, None, str, ],
        'departmentCode': typing.Union[DepartmentCodeSchema, None, decimal.Decimal, int, ],
        'workLocationName': typing.Union[WorkLocationNameSchema, None, str, ],
        'continuationToken': typing.Union[ContinuationTokenSchema, None, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_include = api_client.QueryParameter(
    name="include",
    style=api_client.ParameterStyle.FORM,
    schema=IncludeSchema,
    explode=True,
)
request_query_email_type = api_client.QueryParameter(
    name="emailType",
    style=api_client.ParameterStyle.FORM,
    schema=EmailTypeOptions2Schema,
    explode=True,
)
request_query_status_filter = api_client.QueryParameter(
    name="statusFilter",
    style=api_client.ParameterStyle.FORM,
    schema=EmploymentStatusSchema,
    explode=True,
)
request_query_employee_number = api_client.QueryParameter(
    name="employeeNumber",
    style=api_client.ParameterStyle.FORM,
    schema=EmployeeNumberSchema,
    explode=True,
)
request_query_last_name = api_client.QueryParameter(
    name="lastName",
    style=api_client.ParameterStyle.FORM,
    schema=LastNameSchema,
    explode=True,
)
request_query_department_code = api_client.QueryParameter(
    name="departmentCode",
    style=api_client.ParameterStyle.FORM,
    schema=DepartmentCodeSchema,
    explode=True,
)
request_query_work_location_name = api_client.QueryParameter(
    name="workLocationName",
    style=api_client.ParameterStyle.FORM,
    schema=WorkLocationNameSchema,
    explode=True,
)
request_query_continuation_token = api_client.QueryParameter(
    name="continuationToken",
    style=api_client.ParameterStyle.FORM,
    schema=ContinuationTokenSchema,
    explode=True,
)
# Path params


class LegalEntityIdSchema(
    schemas.Int32Schema
):
    pass
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'legalEntityId': typing.Union[LegalEntityIdSchema, decimal.Decimal, int, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_legal_entity_id = api_client.PathParameter(
    name="legalEntityId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=LegalEntityIdSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = PagedResultOfEmployeeReturnItemSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PagedResultOfEmployeeReturnItem


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PagedResultOfEmployeeReturnItem


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = PaycorErrorSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: PaycorError


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: PaycorError


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = PaycorErrorSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: PaycorError


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: PaycorError


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_by_legal_entity_id_mapped_args(
        self,
        legal_entity_id: int,
        include: typing.Optional[typing.Optional[typing.List[Includes14]]] = None,
        email_type: typing.Optional[EmailTypeOptions2] = None,
        status_filter: typing.Optional[EmploymentStatus] = None,
        employee_number: typing.Optional[typing.Optional[int]] = None,
        last_name: typing.Optional[typing.Optional[str]] = None,
        department_code: typing.Optional[typing.Optional[int]] = None,
        work_location_name: typing.Optional[typing.Optional[str]] = None,
        continuation_token: typing.Optional[typing.Optional[str]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if include is not None:
            _query_params["include"] = include
        if email_type is not None:
            _query_params["emailType"] = email_type
        if status_filter is not None:
            _query_params["statusFilter"] = status_filter
        if employee_number is not None:
            _query_params["employeeNumber"] = employee_number
        if last_name is not None:
            _query_params["lastName"] = last_name
        if department_code is not None:
            _query_params["departmentCode"] = department_code
        if work_location_name is not None:
            _query_params["workLocationName"] = work_location_name
        if continuation_token is not None:
            _query_params["continuationToken"] = continuation_token
        if legal_entity_id is not None:
            _path_params["legalEntityId"] = legal_entity_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _alist_by_legal_entity_id_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Get Employees by Legal Entity ID
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_legal_entity_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_include,
            request_query_email_type,
            request_query_status_filter,
            request_query_employee_number,
            request_query_last_name,
            request_query_department_code,
            request_query_work_location_name,
            request_query_continuation_token,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/legalentities/{legalEntityId}/employees',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _list_by_legal_entity_id_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Get Employees by Legal Entity ID
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_legal_entity_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_include,
            request_query_email_type,
            request_query_status_filter,
            request_query_employee_number,
            request_query_last_name,
            request_query_department_code,
            request_query_work_location_name,
            request_query_continuation_token,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/legalentities/{legalEntityId}/employees',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class ListByLegalEntityIdRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_by_legal_entity_id(
        self,
        legal_entity_id: int,
        include: typing.Optional[typing.Optional[typing.List[Includes14]]] = None,
        email_type: typing.Optional[EmailTypeOptions2] = None,
        status_filter: typing.Optional[EmploymentStatus] = None,
        employee_number: typing.Optional[typing.Optional[int]] = None,
        last_name: typing.Optional[typing.Optional[str]] = None,
        department_code: typing.Optional[typing.Optional[int]] = None,
        work_location_name: typing.Optional[typing.Optional[str]] = None,
        continuation_token: typing.Optional[typing.Optional[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_by_legal_entity_id_mapped_args(
            legal_entity_id=legal_entity_id,
            include=include,
            email_type=email_type,
            status_filter=status_filter,
            employee_number=employee_number,
            last_name=last_name,
            department_code=department_code,
            work_location_name=work_location_name,
            continuation_token=continuation_token,
        )
        return await self._alist_by_legal_entity_id_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def list_by_legal_entity_id(
        self,
        legal_entity_id: int,
        include: typing.Optional[typing.Optional[typing.List[Includes14]]] = None,
        email_type: typing.Optional[EmailTypeOptions2] = None,
        status_filter: typing.Optional[EmploymentStatus] = None,
        employee_number: typing.Optional[typing.Optional[int]] = None,
        last_name: typing.Optional[typing.Optional[str]] = None,
        department_code: typing.Optional[typing.Optional[int]] = None,
        work_location_name: typing.Optional[typing.Optional[str]] = None,
        continuation_token: typing.Optional[typing.Optional[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_by_legal_entity_id_mapped_args(
            legal_entity_id=legal_entity_id,
            include=include,
            email_type=email_type,
            status_filter=status_filter,
            employee_number=employee_number,
            last_name=last_name,
            department_code=department_code,
            work_location_name=work_location_name,
            continuation_token=continuation_token,
        )
        return self._list_by_legal_entity_id_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class ListByLegalEntityId(BaseApi):

    async def alist_by_legal_entity_id(
        self,
        legal_entity_id: int,
        include: typing.Optional[typing.Optional[typing.List[Includes14]]] = None,
        email_type: typing.Optional[EmailTypeOptions2] = None,
        status_filter: typing.Optional[EmploymentStatus] = None,
        employee_number: typing.Optional[typing.Optional[int]] = None,
        last_name: typing.Optional[typing.Optional[str]] = None,
        department_code: typing.Optional[typing.Optional[int]] = None,
        work_location_name: typing.Optional[typing.Optional[str]] = None,
        continuation_token: typing.Optional[typing.Optional[str]] = None,
        validate: bool = False,
        **kwargs,
    ) -> PagedResultOfEmployeeReturnItemPydantic:
        raw_response = await self.raw.alist_by_legal_entity_id(
            legal_entity_id=legal_entity_id,
            include=include,
            email_type=email_type,
            status_filter=status_filter,
            employee_number=employee_number,
            last_name=last_name,
            department_code=department_code,
            work_location_name=work_location_name,
            continuation_token=continuation_token,
            **kwargs,
        )
        if validate:
            return PagedResultOfEmployeeReturnItemPydantic(**raw_response.body)
        return api_client.construct_model_instance(PagedResultOfEmployeeReturnItemPydantic, raw_response.body)
    
    
    def list_by_legal_entity_id(
        self,
        legal_entity_id: int,
        include: typing.Optional[typing.Optional[typing.List[Includes14]]] = None,
        email_type: typing.Optional[EmailTypeOptions2] = None,
        status_filter: typing.Optional[EmploymentStatus] = None,
        employee_number: typing.Optional[typing.Optional[int]] = None,
        last_name: typing.Optional[typing.Optional[str]] = None,
        department_code: typing.Optional[typing.Optional[int]] = None,
        work_location_name: typing.Optional[typing.Optional[str]] = None,
        continuation_token: typing.Optional[typing.Optional[str]] = None,
        validate: bool = False,
    ) -> PagedResultOfEmployeeReturnItemPydantic:
        raw_response = self.raw.list_by_legal_entity_id(
            legal_entity_id=legal_entity_id,
            include=include,
            email_type=email_type,
            status_filter=status_filter,
            employee_number=employee_number,
            last_name=last_name,
            department_code=department_code,
            work_location_name=work_location_name,
            continuation_token=continuation_token,
        )
        if validate:
            return PagedResultOfEmployeeReturnItemPydantic(**raw_response.body)
        return api_client.construct_model_instance(PagedResultOfEmployeeReturnItemPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        legal_entity_id: int,
        include: typing.Optional[typing.Optional[typing.List[Includes14]]] = None,
        email_type: typing.Optional[EmailTypeOptions2] = None,
        status_filter: typing.Optional[EmploymentStatus] = None,
        employee_number: typing.Optional[typing.Optional[int]] = None,
        last_name: typing.Optional[typing.Optional[str]] = None,
        department_code: typing.Optional[typing.Optional[int]] = None,
        work_location_name: typing.Optional[typing.Optional[str]] = None,
        continuation_token: typing.Optional[typing.Optional[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_by_legal_entity_id_mapped_args(
            legal_entity_id=legal_entity_id,
            include=include,
            email_type=email_type,
            status_filter=status_filter,
            employee_number=employee_number,
            last_name=last_name,
            department_code=department_code,
            work_location_name=work_location_name,
            continuation_token=continuation_token,
        )
        return await self._alist_by_legal_entity_id_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        legal_entity_id: int,
        include: typing.Optional[typing.Optional[typing.List[Includes14]]] = None,
        email_type: typing.Optional[EmailTypeOptions2] = None,
        status_filter: typing.Optional[EmploymentStatus] = None,
        employee_number: typing.Optional[typing.Optional[int]] = None,
        last_name: typing.Optional[typing.Optional[str]] = None,
        department_code: typing.Optional[typing.Optional[int]] = None,
        work_location_name: typing.Optional[typing.Optional[str]] = None,
        continuation_token: typing.Optional[typing.Optional[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_by_legal_entity_id_mapped_args(
            legal_entity_id=legal_entity_id,
            include=include,
            email_type=email_type,
            status_filter=status_filter,
            employee_number=employee_number,
            last_name=last_name,
            department_code=department_code,
            work_location_name=work_location_name,
            continuation_token=continuation_token,
        )
        return self._list_by_legal_entity_id_oapg(
            query_params=args.query,
            path_params=args.path,
        )

