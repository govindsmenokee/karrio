from attr import s
from typing import Optional
from jstruct import JStruct


@s(auto_attribs=True)
class GwnStatusType:
    Code: Optional[str] = None
    Description: Optional[str] = None


@s(auto_attribs=True)
class TransactionReferenceType:
    CustomerContext: Optional[str] = None


@s(auto_attribs=True)
class ResponseType:
    ResponseStatus: Optional[GwnStatusType] = JStruct[GwnStatusType]
    Alert: Optional[GwnStatusType] = JStruct[GwnStatusType]
    TransactionReference: Optional[TransactionReferenceType] = JStruct[TransactionReferenceType]


@s(auto_attribs=True)
class PickupCancelResponseClassType:
    Response: Optional[ResponseType] = JStruct[ResponseType]
    PickupType: Optional[str] = None
    GWNStatus: Optional[GwnStatusType] = JStruct[GwnStatusType]


@s(auto_attribs=True)
class PickupCancelResponseType:
    PickupCancelResponse: Optional[PickupCancelResponseClassType] = JStruct[PickupCancelResponseClassType]
