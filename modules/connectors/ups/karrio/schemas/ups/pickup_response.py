from attr import s
from typing import Optional, List
from jstruct import JStruct, JList


@s(auto_attribs=True)
class ChargeDetailType:
    ChargeCode: Optional[str] = None
    ChargeDescription: Optional[str] = None
    ChargeAmount: Optional[str] = None
    IncentedAmount: Optional[str] = None
    TaxAmount: Optional[str] = None


@s(auto_attribs=True)
class RateStatusType:
    Code: Optional[str] = None
    Description: Optional[str] = None


@s(auto_attribs=True)
class TaxChargeType:
    Type: Optional[str] = None
    MonetaryValue: Optional[str] = None


@s(auto_attribs=True)
class RateResultType:
    Disclaimer: Optional[RateStatusType] = JStruct[RateStatusType]
    RateType: Optional[str] = None
    CurrencyCode: Optional[str] = None
    ChargeDetail: List[ChargeDetailType] = JList[ChargeDetailType]
    TaxCharges: List[TaxChargeType] = JList[TaxChargeType]
    TotalTax: Optional[str] = None
    GrandTotalOfAllCharge: Optional[str] = None
    GrandTotalOfAllIncentedCharge: Optional[str] = None
    PreTaxTotalCharge: Optional[str] = None
    PreTaxTotalIncentedCharge: Optional[str] = None


@s(auto_attribs=True)
class TransactionReferenceType:
    CustomerContext: Optional[str] = None
    TransactionIdentifier: Optional[str] = None


@s(auto_attribs=True)
class ResponseType:
    ResponseStatus: Optional[RateStatusType] = JStruct[RateStatusType]
    Alert: Optional[RateStatusType] = JStruct[RateStatusType]
    TransactionReference: Optional[TransactionReferenceType] = JStruct[TransactionReferenceType]


@s(auto_attribs=True)
class WeekendServiceTerritoryType:
    SatWST: Optional[str] = None
    SunWST: Optional[str] = None


@s(auto_attribs=True)
class PickupCreationResponseType:
    Response: Optional[ResponseType] = JStruct[ResponseType]
    PRN: Optional[str] = None
    WeekendServiceTerritory: Optional[WeekendServiceTerritoryType] = JStruct[WeekendServiceTerritoryType]
    WeekendServiceTerritoryIndicator: Optional[str] = None
    RateStatus: Optional[RateStatusType] = JStruct[RateStatusType]
    RateResult: Optional[RateResultType] = JStruct[RateResultType]


@s(auto_attribs=True)
class PickupResponseType:
    PickupCreationResponse: Optional[PickupCreationResponseType] = JStruct[PickupCreationResponseType]
