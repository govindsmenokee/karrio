import karrio.schemas.ups.pickup_response as ups_response
import karrio.schemas.ups.pickup_request as ups
import typing
import karrio.lib as lib
import karrio.core.units as units
import karrio.core.models as models
import karrio.providers.ups.error as provider_error
import karrio.providers.ups.units as provider_units
import karrio.providers.ups.utils as provider_utils


def parse_pickup_response(
    _response: lib.Deserializable[dict],
    settings: provider_utils.Settings,
) -> typing.Tuple[models.PickupDetails, typing.List[models.Message]]:
    response = _response.deserialize()
    details = response.get("PickupCreationResponse")
    pickup = (
        _extract_pickup(details, settings, _response.ctx)
        if details is not None
        else None
    )

    return pickup, provider_error.parse_error_response(response, settings)



def _extract_pickup(
    details: dict,
    settings: provider_utils.Settings,
    ctx: dict,
) -> models.PickupDetails:
    pickup_response = lib.to_object(ups_response.PickupCreationResponseType, details)
    return models.PickupDetails(
        carrier_name=settings.carrier_name,
        carrier_id=settings.carrier_id,
        confirmation_number=pickup_response.PRN
    )



def pickup_request(
    payload: models.PickupRequest,
    settings: provider_utils.Settings,
) -> lib.Serializable:
    shipper = lib.to_address(payload.address)
    packages = lib.to_packages(
        payload.parcels,
        provider_units.PackagePresets,
        package_option_type=provider_units.ShippingOption,
    )
    options = lib.to_shipping_options(
        payload.options,
        package_options=packages.options,
        initializer=provider_units.shipping_options_initializer,
    )
    request = ups.PickupRequestType(
        PickupCreationRequest=ups.PickupCreationRequestType(
            RatePickupIndicator="N",
            Shipper=ups.ShipperType(
                Account=ups.AccountType(AccountNumber=settings.account_number, AccountCountryCode="AE")
            ),
            PickupDateInfo=ups.PickupDateInfoType(
                CloseTime=payload.closing_time[0:5].replace(":", ""),
                ReadyTime=payload.ready_time[0:5].replace(":", ""),
                PickupDate=payload.pickup_date.replace("-", ""),
            ),
            PickupAddress=ups.PickupAddressType(
                CompanyName=shipper.company_name,
                ContactName=shipper.person_name,
                AddressLine=shipper.address_line1,
                City=shipper.city,
                StateProvince=shipper.state_code,
                PostalCode=shipper.postal_code,
                CountryCode=shipper.country_code,
                ResidentialIndicator="Y" if shipper.residential else "N",
                Phone=ups.PhoneType(Number=shipper.phone_number),
            ),
            AlternateAddressIndicator= "Y",
            PickupPiece=[
                ups.PickupPieceType(
                    ServiceCode=provider_units.ServiceCode.map(payload.service_name).value.zfill(3),
                    Quantity="1",
                    DestinationCountryCode=payload.destination_country_code,
                    ContainerCode="01"
                ) for x in payload.parcels
            ],
            TotalWeight=ups.TotalWeightType(
                Weight=str(packages.weight.value),
                UnitOfMeasurement=provider_units.WeightUnit.map(
                    packages.weight_unit
                ).value,
            ),
            PaymentMethod="01",  # Assuming "01" is for the payment method
            SpecialInstruction=payload.instruction
        )
    )

    return lib.Serializable(
        request,
        lib.to_dict,
        dict(),
    )
