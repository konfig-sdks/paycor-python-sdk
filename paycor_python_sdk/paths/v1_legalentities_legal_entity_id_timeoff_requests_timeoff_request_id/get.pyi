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

from paycor_python_sdk.model.paycor_error import PaycorError as PaycorErrorSchema
from paycor_python_sdk.model.employee_time_off_request import EmployeeTimeOffRequest as EmployeeTimeOffRequestSchema

from paycor_python_sdk.type.paycor_error import PaycorError
from paycor_python_sdk.type.employee_time_off_request import EmployeeTimeOffRequest

from ...api_client import Dictionary
from paycor_python_sdk.pydantic.employee_time_off_request import EmployeeTimeOffRequest as EmployeeTimeOffRequestPydantic
from paycor_python_sdk.pydantic.paycor_error import PaycorError as PaycorErrorPydantic

# Path params


class LegalEntityIdSchema(
    schemas.Int32Schema
):
    pass
TimeoffRequestIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'legalEntityId': typing.Union[LegalEntityIdSchema, decimal.Decimal, int, ],
        'timeoffRequestId': typing.Union[TimeoffRequestIdSchema, str, ],
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
request_path_timeoff_request_id = api_client.PathParameter(
    name="timeoffRequestId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=TimeoffRequestIdSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = EmployeeTimeOffRequestSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: EmployeeTimeOffRequest


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: EmployeeTimeOffRequest


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

    def _get_timeoff_request_by_id_mapped_args(
        self,
        legal_entity_id: int,
        timeoff_request_id: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if legal_entity_id is not None:
            _path_params["legalEntityId"] = legal_entity_id
        if timeoff_request_id is not None:
            _path_params["timeoffRequestId"] = timeoff_request_id
        args.path = _path_params
        return args

    async def _aget_timeoff_request_by_id_oapg(
        self,
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
        Get Employee Timeoff Request by Legal Entity Id And Timeoff Request Id
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_legal_entity_id,
            request_path_timeoff_request_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
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
            path_template='/v1/legalentities/{legalEntityId}/timeoffRequests/{timeoffRequestId}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
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


    def _get_timeoff_request_by_id_oapg(
        self,
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
        Get Employee Timeoff Request by Legal Entity Id And Timeoff Request Id
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_legal_entity_id,
            request_path_timeoff_request_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
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
            path_template='/v1/legalentities/{legalEntityId}/timeoffRequests/{timeoffRequestId}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
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


class GetTimeoffRequestByIdRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_timeoff_request_by_id(
        self,
        legal_entity_id: int,
        timeoff_request_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_timeoff_request_by_id_mapped_args(
            legal_entity_id=legal_entity_id,
            timeoff_request_id=timeoff_request_id,
        )
        return await self._aget_timeoff_request_by_id_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get_timeoff_request_by_id(
        self,
        legal_entity_id: int,
        timeoff_request_id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_timeoff_request_by_id_mapped_args(
            legal_entity_id=legal_entity_id,
            timeoff_request_id=timeoff_request_id,
        )
        return self._get_timeoff_request_by_id_oapg(
            path_params=args.path,
        )

class GetTimeoffRequestById(BaseApi):

    async def aget_timeoff_request_by_id(
        self,
        legal_entity_id: int,
        timeoff_request_id: str,
        validate: bool = False,
        **kwargs,
    ) -> EmployeeTimeOffRequestPydantic:
        raw_response = await self.raw.aget_timeoff_request_by_id(
            legal_entity_id=legal_entity_id,
            timeoff_request_id=timeoff_request_id,
            **kwargs,
        )
        if validate:
            return EmployeeTimeOffRequestPydantic(**raw_response.body)
        return api_client.construct_model_instance(EmployeeTimeOffRequestPydantic, raw_response.body)
    
    
    def get_timeoff_request_by_id(
        self,
        legal_entity_id: int,
        timeoff_request_id: str,
        validate: bool = False,
    ) -> EmployeeTimeOffRequestPydantic:
        raw_response = self.raw.get_timeoff_request_by_id(
            legal_entity_id=legal_entity_id,
            timeoff_request_id=timeoff_request_id,
        )
        if validate:
            return EmployeeTimeOffRequestPydantic(**raw_response.body)
        return api_client.construct_model_instance(EmployeeTimeOffRequestPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        legal_entity_id: int,
        timeoff_request_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_timeoff_request_by_id_mapped_args(
            legal_entity_id=legal_entity_id,
            timeoff_request_id=timeoff_request_id,
        )
        return await self._aget_timeoff_request_by_id_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        legal_entity_id: int,
        timeoff_request_id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_timeoff_request_by_id_mapped_args(
            legal_entity_id=legal_entity_id,
            timeoff_request_id=timeoff_request_id,
        )
        return self._get_timeoff_request_by_id_oapg(
            path_params=args.path,
        )

