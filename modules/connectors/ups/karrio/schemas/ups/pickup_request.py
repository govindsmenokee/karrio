from attr import s
from typing import Optional, List
from jstruct import JStruct, JList


@s(auto_attribs=True)
class PhoneType:
    Number: Optional[str] = None
    Extension: Optional[int] = None


@s(auto_attribs=True)
class PickupAddressType:
    CompanyName: Optional[str] = None
    ContactName: Optional[str] = None
    AddressLine: Optional[str] = None
    Room: Optional[str] = None
    Floor: Optional[int] = None
    City: Optional[str] = None
    StateProvince: Optional[str] = None
    Urbanization: Optional[str] = None
    PostalCode: Optional[str] = None
    CountryCode: Optional[str] = None
    ResidentialIndicator: Optional[str] = None
    PickupPoint: Optional[str] = None
    Phone: Optional[PhoneType] = JStruct[PhoneType]


@s(auto_attribs=True)
class PickupDateInfoType:
    CloseTime: Optional[str] = None
    ReadyTime: Optional[str] = None
    PickupDate: Optional[str] = None


@s(auto_attribs=True)
class PickupPieceType:
    ServiceCode: Optional[str] = None
    Quantity: Optional[int] = None
    DestinationCountryCode: Optional[str] = None
    ContainerCode: Optional[str] = None


@s(auto_attribs=True)
class AccountType:
    AccountNumber: Optional[str] = None
    AccountCountryCode: Optional[str] = None


@s(auto_attribs=True)
class ShipperType:
    Account: Optional[AccountType] = JStruct[AccountType]


@s(auto_attribs=True)
class TotalWeightType:
    Weight: Optional[str] = None
    UnitOfMeasurement: Optional[str] = None


@s(auto_attribs=True)
class PickupCreationRequestType:
    RatePickupIndicator: Optional[str] = None
    Shipper: Optional[ShipperType] = JStruct[ShipperType]
    PickupDateInfo: Optional[PickupDateInfoType] = JStruct[PickupDateInfoType]
    PickupAddress: Optional[PickupAddressType] = JStruct[PickupAddressType]
    AlternateAddressIndicator: Optional[str] = None
    PickupPiece: List[PickupPieceType] = JList[PickupPieceType]
    TotalWeight: Optional[TotalWeightType] = JStruct[TotalWeightType]
    OverweightIndicator: Optional[str] = None
    PaymentMethod: Optional[str] = None
    SpecialInstruction: Optional[str] = None
    ReferenceNumber: Optional[str] = None


@s(auto_attribs=True)
class PickupRequestType:
    PickupCreationRequest: Optional[PickupCreationRequestType] = JStruct[PickupCreationRequestType]
