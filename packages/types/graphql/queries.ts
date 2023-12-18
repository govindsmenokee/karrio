import gql from 'graphql-tag';


export const GET_ADDRESS_TEMPLATES = gql`query get_address_templates($filter: AddressFilter) {
  address_templates(filter: $filter) {
    page_info {
      has_next_page
      has_previous_page
      start_cursor
      end_cursor
    }
    edges {
      node {
        id
        is_default
        label
        address {
          company_name
          person_name
          street_number
          address_line1
          address_line2
          postal_code
          residential
          city
          state_code
          country_code
          email
          phone_number
          federal_tax_id
          state_tax_id
          validate_location
        }
      }
    }
  }
}
`;

export const GET_CUSTOMS_TEMPLATES = gql`query get_customs_info_templates($filter: TemplateFilter) {
  customs_templates(filter: $filter) {
    page_info {
      has_next_page
      has_previous_page
      start_cursor
      end_cursor
    }
    edges {
      node {
        id
        label
        is_default
        customs {
          incoterm
          content_type
          commercial_invoice
          content_description
          duty {
            paid_by
            currency
            account_number
            declared_value
          }
          invoice
          invoice_date
          signer
          certify
          options
        }
      }
    }
  }
}
`;

export const GET_DEFAULT_TEMPLATES = gql`query get_default_templates {
  default_templates {
    default_address {
      id
      is_default
      label
      address {
        company_name
        person_name
        street_number
        address_line1
        address_line2
        postal_code
        residential
        city
        state_code
        country_code
        email
        phone_number
        federal_tax_id
        state_tax_id
        validate_location
      }
    }
    default_customs {
      id
      label
      is_default
      customs {
        incoterm
        content_type
        commercial_invoice
        content_description
        duty {
          paid_by
          currency
          account_number
          declared_value
        }
        invoice
        invoice_date
        signer
        certify
        options
      }
    }
    default_parcel {
      id
      is_default
      label
      parcel {
        width
        height
        length
        dimension_unit
        weight
        weight_unit
        packaging_type
        package_preset
        is_document
      }
    }
  }
}
`;

export const CREATE_CARRIER_CONNECTION = gql`mutation create_connection($data: CreateCarrierConnectionMutationInput!) {
  create_carrier_connection(input: $data) {
    errors {
      field
      messages
    }
  }
}
`;

export const UPDATE_CARRIER_CONNECTION = gql`mutation update_connection($data: UpdateCarrierConnectionMutationInput!) {
  update_carrier_connection(input: $data) {
    errors {
      field
      messages
    }
  }
}
`;

export const DELETE_CARRIER_CONNECTION = gql`mutation delete_connection($data: DeleteMutationInput!) {
  delete_carrier_connection(input: $data) {
    id
  }
}
`;

export const GET_ORGANIZATION = gql`query get_organization($id: String!) {
  organization(id: $id) {
    id
    name
    slug
    token
    current_user {
      email
      full_name
      is_admin
      is_owner
      last_login
    }
    members {
      email
      full_name
      is_admin
      is_owner
      invitation {
        id
        guid
        invitee_identifier
        created
        modified
      }
      last_login
    }
    usage {
      members
      order_volume
      total_requests
      total_shipments
      unfulfilled_orders
      api_requests {
        date
        label
        count
      }
      order_volumes {
        date
        label
        count
      }
      shipment_count {
        date
        label
        count
      }
      shipment_spend {
        date
        label
        count
      }
    }
  }
}
`;

export const GET_ORGANIZATIONS = gql`query get_organizations {
  organizations {
    id
    name
    slug
    token
    current_user {
      email
      full_name
      is_admin
      is_owner
      last_login
    }
    members {
      email
      full_name
      is_admin
      is_owner
      invitation {
        id
        guid
        invitee_identifier
        created
        modified
      }
      last_login
    }
    usage {
      members
      order_volume
      total_requests
      total_shipments
      unfulfilled_orders
      api_requests {
        date
        label
        count
      }
      order_volumes {
        date
        label
        count
      }
      shipment_count {
        date
        label
        count
      }
      shipment_spend {
        date
        label
        count
      }
    }
  }
}
`;

export const DELETE_ORGANIZATION = gql`mutation delete_organization($data: DeleteOrganizationMutationInput!) {
  delete_organization(input: $data) {
    organization {
      id
    }
    errors {
      field
      messages
    }
  }
}
`;

export const CREATE_ORGANIZATION = gql`mutation create_organization($data: CreateOrganizationMutationInput!) {
  create_organization(input: $data) {
    organization {
      id
    }
    errors {
      field
      messages
    }
  }
}
`;

export const UPDATE_ORGANIZATION = gql`mutation update_organization($data: UpdateOrganizationMutationInput!) {
  update_organization(input: $data) {
    organization {
      id
    }
    errors {
      field
      messages
    }
  }
}
`;

export const CHANGE_ORGANIZATION_OWNER = gql`mutation change_organization_owner($data: ChangeOrganizationOwnerMutationInput!) {
  change_organization_owner(input: $data) {
    organization {
      id
    }
    errors {
      field
      messages
    }
  }
}
`;

export const SET_ORGANIZATION_USER_ROLES = gql`mutation set_organization_user_roles($data: SetOrganizationUserRolesMutationInput!) {
  set_organization_user_roles(input: $data) {
    organization {
      id
    }
    errors {
      field
      messages
    }
  }
}
`;

export const SEND_ORGANIZATION_INVITES = gql`mutation send_organization_invites($data: SendOrganizationInvitesMutationInput!) {
  send_organization_invites(input: $data) {
    errors {
      field
      messages
    }
  }
}
`;

export const GET_ORGANIZATION_INVITATION = gql`query get_organization_invitation($guid: String!) {
  organization_invitation(guid: $guid) {
    invitee_identifier
    organization_name
    invitee {
      email
    }
  }
}
`;

export const ACCEPT_ORGANIZATION_INVITATION = gql`mutation accept_organization_invitation($data: AcceptOrganizationInvitationMutationInput!) {
  accept_organization_invitation(input: $data) {
    organization {
      id
    }
    errors {
      field
      messages
    }
  }
}
`;

export const DELETE_ORGANIZATION_INVITES = gql`mutation delete_organization_invitation($data: DeleteMutationInput!) {
  delete_organization_invitation(input: $data) {
    id
  }
}
`;

export const GET_LOG = gql`query get_log($id: Int!) {
  log(id: $id) {
    id
    requested_at
    response_ms
    path
    remote_addr
    host
    method
    query_params
    data
    response
    status_code
    records {
      id
      key
      timestamp
      test_mode
      created_at
      meta
      record
    }
  }
}
`;

export const GET_LOGS = gql`query get_logs($filter: LogFilter) {
  logs(filter: $filter) {
    page_info {
      has_next_page
      has_previous_page
      start_cursor
      end_cursor
    }
    edges {
      node {
        id
        path
        host
        data
        method
        response_ms
        remote_addr
        requested_at
        status_code
        query_params
        response
        records {
          id
          key
          timestamp
          test_mode
          created_at
          meta
          record
        }
      }
    }
  }
}
`;

export const GET_SHIPMENT = gql`query get_shipment($id: String!) {
  shipment(id: $id) {
    id
    carrier_id
    carrier_name
    created_at
    updated_at
    created_by {
      email
      full_name
    }
    status
    recipient {
      id
      postal_code
      city
      person_name
      company_name
      country_code
      email
      phone_number
      state_code
      suburb
      residential
      street_number
      address_line1
      address_line2
      federal_tax_id
      state_tax_id
      validate_location
    }
    shipper {
      id
      postal_code
      city
      person_name
      company_name
      country_code
      email
      phone_number
      state_code
      suburb
      residential
      street_number
      address_line1
      address_line2
      federal_tax_id
      state_tax_id
      validate_location
    }
    billing_address {
      id
      postal_code
      city
      person_name
      company_name
      country_code
      email
      phone_number
      state_code
      suburb
      residential
      street_number
      address_line1
      address_line2
      federal_tax_id
      state_tax_id
      validate_location
    }
    parcels {
      id
      width
      height
      length
      is_document
      dimension_unit
      weight
      weight_unit
      packaging_type
      package_preset
      freight_class
      reference_number
      items {
        id
        weight
        title
        description
        quantity
        sku
        hs_code
        value_amount
        weight_unit
        value_currency
        origin_country
        metadata
        parent_id
      }
    }
    label_type
    tracking_number
    shipment_identifier
    label_url
    invoice_url
    tracking_url
    tracker_id
    test_mode
    service
    reference
    customs {
      id
      certify
      commercial_invoice
      content_type
      content_description
      incoterm
      invoice
      invoice_date
      signer
      duty {
        paid_by
        currency
        account_number
        declared_value
      }
      options
      commodities {
        id
        weight
        weight_unit
        title
        description
        quantity
        sku
        hs_code
        value_amount
        value_currency
        origin_country
        metadata
        parent_id
      }
      duty_billing_address {
        id
        postal_code
        city
        person_name
        company_name
        country_code
        email
        phone_number
        state_code
        suburb
        residential
        street_number
        address_line1
        address_line2
        federal_tax_id
        state_tax_id
        validate_location
      }
    }
    payment {
      paid_by
      currency
      account_number
    }
    selected_rate_id
    selected_rate {
      id
      carrier_name
      carrier_id
      currency
      service
      transit_days
      total_charge
      extra_charges {
        name
        amount
        currency
      }
      test_mode
      meta
    }
    carrier_ids
    rates {
      id
      carrier_name
      carrier_id
      currency
      service
      transit_days
      total_charge
      extra_charges {
        name
        amount
        currency
      }
      test_mode
      meta
    }
    options
    metadata
    meta
    messages {
      carrier_name
      carrier_id
      message
      code
      details
    }
    tracker {
      id
      tracking_number
      carrier_id
      carrier_name
      status
      events {
        description
        location
        code
        date
        time
        latitude
        longitude
      }
      delivered
      estimated_delivery
      meta
      metadata
      info {
        carrier_tracking_link
        customer_name
        expected_delivery
        note
        order_date
        order_id
        package_weight
        package_weight_unit
        shipment_package_count
        shipment_pickup_date
        shipment_service
        shipment_delivery_date
        shipment_origin_country
        shipment_origin_postal_code
        shipment_destination_country
        shipment_destination_postal_code
        shipping_date
        signed_by
        source
      }
      messages {
        carrier_name
        carrier_id
        message
        code
        details
      }
      updated_at
    }
  }
}
`;

export const GET_SHIPMENTS = gql`query get_shipments($filter: ShipmentFilter) {
  shipments(filter: $filter) {
    page_info {
      has_next_page
      has_previous_page
      start_cursor
      end_cursor
    }
    edges {
      node {
        id
        carrier_id
        carrier_name
        created_at
        updated_at
        created_by {
          email
          full_name
        }
        status
        recipient {
          id
          postal_code
          city
          person_name
          company_name
          country_code
          email
          phone_number
          state_code
          suburb
          residential
          street_number
          address_line1
          address_line2
          federal_tax_id
          state_tax_id
          validate_location
        }
        shipper {
          id
          postal_code
          city
          person_name
          company_name
          country_code
          email
          phone_number
          state_code
          suburb
          residential
          street_number
          address_line1
          address_line2
          federal_tax_id
          state_tax_id
          validate_location
        }
        billing_address {
          id
          postal_code
          city
          person_name
          company_name
          country_code
          email
          phone_number
          state_code
          suburb
          residential
          street_number
          address_line1
          address_line2
          federal_tax_id
          state_tax_id
          validate_location
        }
        parcels {
          id
          width
          height
          length
          is_document
          dimension_unit
          weight
          weight_unit
          packaging_type
          package_preset
          freight_class
          reference_number
          items {
            id
            weight
            title
            description
            quantity
            sku
            hs_code
            value_amount
            weight_unit
            value_currency
            origin_country
            metadata
            parent_id
          }
        }
        label_type
        tracking_number
        shipment_identifier
        label_url
        invoice_url
        tracking_url
        tracker_id
        test_mode
        service
        reference
        customs {
          id
          certify
          commercial_invoice
          content_type
          content_description
          incoterm
          invoice
          invoice_date
          signer
          duty {
            paid_by
            currency
            account_number
            declared_value
          }
          options
          commodities {
            id
            weight
            weight_unit
            title
            description
            quantity
            sku
            hs_code
            value_amount
            value_currency
            origin_country
            metadata
            parent_id
          }
          duty_billing_address {
            id
            postal_code
            city
            person_name
            company_name
            country_code
            email
            phone_number
            state_code
            suburb
            residential
            street_number
            address_line1
            address_line2
            federal_tax_id
            state_tax_id
            validate_location
          }
        }
        payment {
          paid_by
          currency
          account_number
        }
        selected_rate_id
        selected_rate {
          id
          carrier_name
          carrier_id
          currency
          service
          transit_days
          total_charge
          extra_charges {
            name
            amount
            currency
          }
          test_mode
          meta
        }
        carrier_ids
        rates {
          id
          carrier_name
          carrier_id
          currency
          service
          transit_days
          total_charge
          extra_charges {
            name
            amount
            currency
          }
          test_mode
          meta
        }
        options
        metadata
        meta
        messages {
          carrier_name
          carrier_id
          message
          code
          details
        }
      }
    }
  }
}
`;

export const GET_SHIPMENT_DATA = gql`query get_shipment_data($id: String!) {
  shipment(id: $id) {
    id
    status
    recipient {
      id
      postal_code
      city
      person_name
      company_name
      country_code
      email
      phone_number
      state_code
      suburb
      residential
      street_number
      address_line1
      address_line2
      federal_tax_id
      state_tax_id
      validate_location
    }
    shipper {
      id
      postal_code
      city
      person_name
      company_name
      country_code
      email
      phone_number
      state_code
      suburb
      residential
      street_number
      address_line1
      address_line2
      federal_tax_id
      state_tax_id
      validate_location
    }
    billing_address {
      id
      postal_code
      city
      person_name
      company_name
      country_code
      email
      phone_number
      state_code
      suburb
      residential
      street_number
      address_line1
      address_line2
      federal_tax_id
      state_tax_id
      validate_location
    }
    parcels {
      id
      width
      height
      length
      is_document
      dimension_unit
      weight
      weight_unit
      packaging_type
      package_preset
      freight_class
      reference_number
      items {
        id
        weight
        title
        description
        quantity
        sku
        hs_code
        value_amount
        weight_unit
        value_currency
        origin_country
        metadata
        parent_id
      }
    }
    label_type
    service
    reference
    customs {
      id
      certify
      commercial_invoice
      content_type
      content_description
      incoterm
      invoice
      invoice_date
      signer
      duty {
        paid_by
        currency
        account_number
        declared_value
      }
      options
      commodities {
        id
        weight
        weight_unit
        title
        description
        quantity
        sku
        hs_code
        value_amount
        value_currency
        origin_country
        metadata
        parent_id
      }
      duty_billing_address {
        id
        postal_code
        city
        person_name
        company_name
        country_code
        email
        phone_number
        state_code
        suburb
        residential
        street_number
        address_line1
        address_line2
        federal_tax_id
        state_tax_id
        validate_location
      }
    }
    payment {
      paid_by
      currency
      account_number
    }
    carrier_ids
    options
    metadata
    rates {
      id
      carrier_name
      carrier_id
      currency
      service
      transit_days
      total_charge
      extra_charges {
        name
        amount
        currency
      }
      test_mode
      meta
    }
    messages {
      carrier_name
      carrier_id
      message
      code
      details
    }
  }
}
`;

export const PARTIAL_UPDATE_SHIPMENT = gql`mutation partial_shipment_update($data: PartialShipmentMutationInput!) {
  partial_shipment_update(input: $data) {
    shipment {
      id
      status
      recipient {
        id
        postal_code
        city
        person_name
        company_name
        country_code
        email
        phone_number
        state_code
        suburb
        residential
        street_number
        address_line1
        address_line2
        federal_tax_id
        state_tax_id
        validate_location
      }
      shipper {
        id
        postal_code
        city
        person_name
        company_name
        country_code
        email
        phone_number
        state_code
        suburb
        residential
        street_number
        address_line1
        address_line2
        federal_tax_id
        state_tax_id
        validate_location
      }
      billing_address {
        id
        postal_code
        city
        person_name
        company_name
        country_code
        email
        phone_number
        state_code
        suburb
        residential
        street_number
        address_line1
        address_line2
        federal_tax_id
        state_tax_id
        validate_location
      }
      parcels {
        id
        width
        height
        length
        is_document
        dimension_unit
        weight
        weight_unit
        packaging_type
        package_preset
        freight_class
        reference_number
        items {
          id
          weight
          title
          description
          quantity
          sku
          hs_code
          value_amount
          weight_unit
          value_currency
          origin_country
          metadata
          parent_id
        }
      }
      label_type
      service
      reference
      customs {
        id
        certify
        commercial_invoice
        content_type
        content_description
        incoterm
        invoice
        invoice_date
        signer
        duty {
          paid_by
          currency
          account_number
          declared_value
        }
        options
        commodities {
          id
          weight
          weight_unit
          title
          description
          quantity
          sku
          hs_code
          value_amount
          value_currency
          origin_country
          metadata
          parent_id
        }
        duty_billing_address {
          id
          postal_code
          city
          person_name
          company_name
          country_code
          email
          phone_number
          state_code
          suburb
          residential
          street_number
          address_line1
          address_line2
          federal_tax_id
          state_tax_id
          validate_location
        }
      }
      payment {
        paid_by
        currency
        account_number
      }
      carrier_ids
      options
      metadata
      rates {
        id
        carrier_name
        carrier_id
        currency
        service
        transit_days
        total_charge
        extra_charges {
          name
          amount
          currency
        }
        test_mode
        meta
      }
      messages {
        carrier_name
        carrier_id
        message
        code
        details
      }
    }
    errors {
      field
      messages
    }
  }
}
`;

export const CHANGE_SHIPMENT_STATUS = gql`mutation change_shipment_status($data: ChangeShipmentStatusMutationInput!) {
  change_shipment_status(input: $data) {
    shipment {
      id
    }
    errors {
      field
      messages
    }
  }
}
`;

export const GET_TRACKER = gql`query get_tracker($id: String!) {
  tracker(id: $id) {
    id
    tracking_number
    carrier_id
    carrier_name
    status
    events {
      description
      location
      code
      date
      time
      latitude
      longitude
    }
    delivered
    estimated_delivery
    meta
    metadata
    info {
      carrier_tracking_link
      customer_name
      expected_delivery
      note
      order_date
      order_id
      package_weight
      package_weight_unit
      shipment_package_count
      shipment_pickup_date
      shipment_service
      shipment_delivery_date
      shipment_origin_country
      shipment_origin_postal_code
      shipment_destination_country
      shipment_destination_postal_code
      shipping_date
      signed_by
      source
    }
    messages {
      carrier_name
      carrier_id
      message
      code
      details
    }
    created_at
    updated_at
    created_by {
      email
      full_name
    }
    test_mode
    shipment {
      id
      service
      shipper {
        city
        country_code
      }
      recipient {
        city
        country_code
      }
      meta
      reference
    }
  }
}`;

export const GET_TRACKERS = gql`query get_trackers($filter: TrackerFilter) {
  trackers(filter: $filter) {
    page_info {
      has_next_page
      has_previous_page
      start_cursor
      end_cursor
    }
    edges {
      node {
        id
        created_at
        updated_at
        created_by {
          email
          full_name
        }
        status
        tracking_number
        events {
          description
          location
          code
          date
          time
          latitude
          longitude
        }
        delivered
        estimated_delivery
        test_mode
        info {
          carrier_tracking_link
          customer_name
          expected_delivery
          note
          order_date
          order_id
          package_weight
          package_weight_unit
          shipment_package_count
          shipment_pickup_date
          shipment_service
          shipment_delivery_date
          shipment_origin_country
          shipment_origin_postal_code
          shipment_destination_country
          shipment_destination_postal_code
          shipping_date
          signed_by
          source
        }
        messages {
          carrier_name
          carrier_id
          message
          code
          details
        }
        carrier_id
        carrier_name
        meta
        metadata
        shipment {
          id
          service
          shipper {
            city
            country_code
          }
          recipient {
            city
            country_code
          }
          meta
          reference
        }
      }
    }
  }
}
`;

export const GET_WEBHOOK = gql`query get_webhook($id: String!) {
  webhook(id: $id) {
    id
    created_by {
      email
      full_name
    }
    enabled_events
    url
    test_mode
    disabled
    description
    last_event_at
    secret
  }
}
`;

export const GET_WEBHOOKS = gql`query get_webhooks($filter: WebhookFilter) {
  webhooks(filter: $filter) {
    page_info {
      has_next_page
      has_previous_page
      start_cursor
      end_cursor
    }
    edges {
      node {
        id
        created_at
        updated_at
        created_by {
          email
          full_name
        }
        enabled_events
        url
        test_mode
        disabled
        description
        last_event_at
        secret
      }
    }
  }
}
`;

export const GET_PARCEL_TEMPLATES = gql`query get_parcel_templates($filter: TemplateFilter) {
  parcel_templates(filter: $filter) {
    page_info {
      has_next_page
      has_previous_page
      start_cursor
      end_cursor
    }
    edges {
      node {
        id
        is_default
        label
        parcel {
          width
          height
          length
          dimension_unit
          weight
          weight_unit
          packaging_type
          package_preset
          is_document
        }
      }
    }
  }
}
`;

export const GET_SYSTEM_CONNECTIONS = gql`query get_system_connections {
  system_connections {
    id
    carrier_id
    test_mode
    active
    capabilities
    carrier_name
    display_name
    enabled
  }
}
`;

export const MUTATE_SYSTEM_CONNECTION = gql`mutation mutate_system_connection($data: SystemCarrierMutationInput!) {
  mutate_system_connection(input: $data) {
    carrier {
      id
      active
    }
  }
}
`;

export const CREATE_CUSTOMS_TEMPLATE = gql`mutation create_customs_template($data: CreateCustomsTemplateInput!) {
  create_customs_template(input: $data) {
    template {
      id
    }
    errors {
      field
      messages
    }
  }
}
`;

export const UPDATE_CUSTOMS_TEMPLATE = gql`mutation update_customs_template($data: UpdateCustomsTemplateInput!) {
  update_customs_template(input: $data) {
    template {
      id
    }
    errors {
      field
      messages
    }
  }
}
`;

export const DELETE_TEMPLATE = gql`mutation delete_template($data: DeleteMutationInput!) {
  delete_template(input: $data) {
    id
  }
}
`;

export const CREATE_PARCEL_TEMPLATE = gql`mutation create_parcel_template($data: CreateParcelTemplateInput!) {
  create_parcel_template(input: $data) {
    template {
      id
    }
    errors {
      field
      messages
    }
  }
}
`;

export const UPDATE_PARCEL_TEMPLATE = gql`mutation update_parcel_template($data: UpdateParcelTemplateInput!) {
  update_parcel_template(input: $data) {
    template {
      id
    }
    errors {
      field
      messages
    }
  }
}
`;

export const CREATE_ADDRESS_TEMPLATE = gql`mutation create_address_template($data: CreateAddressTemplateInput!) {
  create_address_template(input: $data) {
    template {
      id
    }
    errors {
      field
      messages
    }
  }
}
`;

export const UPDATE_ADDRESS_TEMPLATE = gql`mutation update_address_template($data: UpdateAddressTemplateInput!) {
  update_address_template(input: $data) {
    template {
      id
    }
    errors {
      field
      messages
    }
  }
}
`;

export const DISCARD_COMMODITY = gql`mutation discard_commodity($data: DeleteMutationInput!) {
  discard_commodity(input: $data) {
    id
  }
}
`;

export const DISCARD_CUSTOMS = gql`mutation discard_customs($data: DeleteMutationInput!) {
  discard_customs(input: $data) {
    id
  }
}
`;

export const DISCARD_PARCEL = gql`mutation discard_parcel($data: DeleteMutationInput!) {
  discard_parcel(input: $data) {
    id
  }
}
`;

export const MUTATE_API_TOKEN = gql`mutation mutate_token($data: TokenMutationInput!) {
  mutate_token(input: $data) {
    token {
      key
    }
  }
}
`;

export const GET_API_TOKEN = gql`query GetToken($org_id: String) {
  token(org_id: $org_id) {
    key
    created
  }
}
`;

export const GET_USER_CONNECTIONS = gql`query get_user_connections {
  user_connections {
    __typename
    ... on AlliedExpressSettingsType {
      id
      carrier_id
      carrier_name
      display_name
      test_mode
      active
      capabilities
      metadata
      config
      username
      password
      account
    }
    ... on AmazonShippingSettingsType {
      id
      carrier_id
      carrier_name
      display_name
      test_mode
      active
      capabilities
      metadata
      seller_id
      developer_id
      mws_auth_token
      aws_region
      config
    }
    ... on AramexSettingsType {
      id
      carrier_id
      carrier_name
      display_name
      test_mode
      active
      capabilities
      metadata
      username
      password
      account_pin
      account_entity
      account_number
      account_country_code
      config
    }
    ... on AsendiaUSSettingsType {
      id
      carrier_id
      carrier_name
      display_name
      test_mode
      active
      capabilities
      metadata
      username
      password
      account_number
      api_key
      config
    }
    ... on AustraliaPostSettingsType {
      id
      carrier_id
      carrier_name
      display_name
      test_mode
      active
      capabilities
      metadata
      api_key
      password
      account_number
      config
    }
    ... on BoxKnightSettingsType {
      id
      carrier_id
      carrier_name
      display_name
      test_mode
      active
      capabilities
      username
      password
      config
      metadata
    }
    ... on BelgianPostSettingsType {
      id
      carrier_id
      carrier_name
      display_name
      test_mode
      active
      capabilities
      metadata
      config
      account_id
      passphrase
      services {
        id
        active
        service_name
        service_code
        description
        currency
        transit_days
        transit_time
        max_weight
        max_width
        max_height
        max_length
        weight_unit
        dimension_unit
        domicile
        international
        zones {
          label
          rate
          min_weight
          max_weight
          transit_days
          transit_time
          radius
          latitude
          longitude
          cities
          country_codes
        }
      }
      rate_sheet {
        id
        name
        slug
        carrier_name
        metadata
      }
    }
    ... on CanadaPostSettingsType {
      id
      carrier_id
      carrier_name
      display_name
      test_mode
      active
      capabilities
      metadata
      username
      password
      customer_number
      contract_id
      config
    }
    ... on CanparSettingsType {
      id
      carrier_id
      carrier_name
      display_name
      test_mode
      active
      metadata
      capabilities
      username
      password
      config
    }
    ... on ChronopostSettingsType {
      id
      carrier_id
      carrier_name
      display_name
      test_mode
      active
      metadata
      capabilities
      password
      account_number
      account_country_code
      config
    }
    ... on ColissimoSettingsType {
      id
      carrier_id
      carrier_name
      display_name
      test_mode
      active
      capabilities
      metadata
      config
      password
      contract_number
      laposte_api_key
      services {
        id
        active
        service_name
        service_code
        description
        currency
        transit_days
        transit_time
        max_weight
        max_width
        max_height
        max_length
        weight_unit
        dimension_unit
        domicile
        international
        zones {
          label
          rate
          min_weight
          max_weight
          transit_days
          transit_time
          radius
          latitude
          longitude
          cities
          country_codes
        }
      }
      rate_sheet {
        id
        name
        slug
        carrier_name
        metadata
      }
    }
    ... on DHLExpressSettingsType {
      id
      carrier_id
      carrier_name
      display_name
      test_mode
      active
      metadata
      capabilities
      site_id
      password
      account_number
      account_country_code
      config
    }
    ... on DHLPolandSettingsType {
      id
      carrier_id
      carrier_name
      display_name
      test_mode
      active
      capabilities
      metadata
      config
      username
      password
      account_number
      services {
        id
        active
        service_name
        service_code
        description
        currency
        transit_days
        transit_time
        max_weight
        max_width
        max_height
        max_length
        weight_unit
        dimension_unit
        domicile
        international
        zones {
          label
          rate
          min_weight
          max_weight
          transit_days
          transit_time
          radius
          latitude
          longitude
          cities
          country_codes
        }
      }
      rate_sheet {
        id
        name
        slug
        carrier_name
        metadata
      }
    }
    ... on DHLUniversalSettingsType {
      id
      carrier_id
      carrier_name
      display_name
      test_mode
      active
      metadata
      capabilities
      consumer_key
      consumer_secret
      config
    }
    ... on DicomSettingsType {
      id
      carrier_id
      carrier_name
      display_name
      test_mode
      active
      metadata
      capabilities
      username
      password
      billing_account
      config
    }
    ... on DPDSettingsType {
      id
      carrier_id
      carrier_name
      display_name
      test_mode
      active
      metadata
      config
      capabilities
      delis_id
      password
      depot
      account_country_code
      services {
        active
        currency
        description
        dimension_unit
        domicile
        id
        international
        max_height
        max_length
        max_weight
        max_width
        service_code
        service_name
        transit_days
        transit_time
        weight_unit
        zones {
          cities
          country_codes
          label
          latitude
          longitude
          max_weight
          min_weight
          radius
          rate
          transit_days
          transit_time
        }
      }
      rate_sheet {
        id
        name
        slug
        carrier_name
        metadata
      }
    }
    ... on DPDHLSettingsType {
      id
      carrier_id
      carrier_name
      display_name
      test_mode
      active
      metadata
      capabilities
      username
      password
      app_id
      app_token
      zt_id
      zt_password
      account_number
      config
      services {
        id
        active
        service_name
        service_code
        description
        currency
        transit_days
        transit_time
        max_weight
        max_width
        max_height
        max_length
        weight_unit
        dimension_unit
        domicile
        international
        zones {
          label
          rate
          min_weight
          max_weight
          transit_days
          transit_time
          radius
          latitude
          longitude
          cities
          country_codes
        }
      }
      rate_sheet {
        id
        name
        slug
        carrier_name
        metadata
      }
    }
    ... on EShipperSettingsType {
      id
      carrier_id
      carrier_name
      display_name
      test_mode
      active
      metadata
      capabilities
      username
      password
      config
    }
    ... on EasyPostSettingsType {
      id
      carrier_id
      carrier_name
      display_name
      test_mode
      active
      metadata
      capabilities
      api_key
      config
    }
    ... on FedexSettingsType {
      id
      carrier_id
      carrier_name
      display_name
      test_mode
      active
      metadata
      capabilities
      account_number
      password
      meter_number
      user_key
      account_country_code
      config
    }
    ... on FreightcomSettingsType {
      id
      carrier_id
      carrier_name
      display_name
      test_mode
      active
      metadata
      capabilities
      username
      password
      config
    }
    ... on GenericSettingsType {
      id
      carrier_id
      carrier_name
      display_name
      custom_carrier_name
      account_number
      test_mode
      active
      metadata
      config
      capabilities
      account_country_code
      services {
        id
        active
        service_name
        service_code
        description
        currency
        transit_days
        transit_time
        max_weight
        max_width
        max_height
        max_length
        weight_unit
        dimension_unit
        domicile
        international
        zones {
          label
          rate
          min_weight
          max_weight
          transit_days
          transit_time
          radius
          latitude
          longitude
          cities
          country_codes
        }
      }
      label_template {
        id
        slug
        template
        template_type
        shipment_sample
        width
        height
      }
      rate_sheet {
        id
        name
        slug
        carrier_name
        metadata
      }
    }
    ... on GEODISSettingsType {
      id
      carrier_id
      carrier_name
      display_name
      test_mode
      active
      metadata
      capabilities
      api_key
      identifier
      language
      config
    }
    ... on LaPosteSettingsType {
      id
      carrier_id
      carrier_name
      display_name
      test_mode
      active
      metadata
      capabilities
      api_key
      lang
      config
    }
    ... on Locate2uSettingsType {
      id
      carrier_id
      carrier_name
      display_name
      test_mode
      active
      capabilities
      metadata
      config
      account_country_code
      client_id
      client_secret
    }
    ... on NationexSettingsType {
      id
      carrier_id
      carrier_name
      display_name
      test_mode
      active
      metadata
      capabilities
      api_key
      customer_id
      billing_account
      language
      config
    }
    ... on PurolatorSettingsType {
      id
      carrier_id
      carrier_name
      display_name
      test_mode
      active
      metadata
      capabilities
      username
      password
      account_number
      user_token
      config
    }
    ... on RoadieSettingsType {
      id
      carrier_id
      carrier_name
      display_name
      test_mode
      active
      metadata
      capabilities
      api_key
      config
    }
    ... on RoyalMailSettingsType {
      id
      carrier_id
      carrier_name
      display_name
      test_mode
      active
      metadata
      capabilities
      client_id
      client_secret
      config
    }
    ... on SendleSettingsType {
      id
      carrier_id
      carrier_name
      display_name
      test_mode
      active
      metadata
      capabilities
      sendle_id
      api_key
      config
    }
    ... on TNTSettingsType {
      id
      carrier_id
      carrier_name
      display_name
      test_mode
      active
      metadata
      capabilities
      username
      password
      account_number
      account_country_code
      config
    }
    ... on UPSSettingsType {
      id
      carrier_id
      carrier_name
      display_name
      test_mode
      active
      metadata
      capabilities
      client_id
      client_secret
      account_number
      account_country_code
      config
    }
    ... on USPSSettingsType {
      id
      carrier_id
      carrier_name
      display_name
      test_mode
      active
      metadata
      capabilities
      username
      password
      mailer_id
      customer_registration_id
      logistics_manager_mailer_id
      config
    }
    ... on USPSInternationalSettingsType {
      id
      carrier_id
      carrier_name
      display_name
      test_mode
      active
      metadata
      capabilities
      username
      password
      mailer_id
      customer_registration_id
      logistics_manager_mailer_id
      config
    }
    ... on Zoom2uSettingsType {
      id
      carrier_id
      carrier_name
      display_name
      test_mode
      active
      capabilities
      metadata
      config
      account_country_code
      api_key
    }
  }
}`;

export const GET_USER = gql`query GetUser {
  user {
    email
    full_name
    is_staff
    is_superuser
    last_login
    date_joined
    permissions
  }
}
`;

export const UPDATE_USER = gql`mutation update_user($data: UpdateUserInput!) {
  update_user(input: $data) {
    user {
      email
      full_name
      is_staff
      is_superuser
      last_login
      date_joined
      permissions
    }
    errors {
      field
      messages
    }
  }
}
`;

export const CHANGE_PASSWORD = gql`mutation change_password($data: ChangePasswordMutationInput!) {
  change_password(input: $data) {
    errors {
      field
      messages
    }
  }
}
`;

export const REGISTER_USER = gql`mutation register_user($data: RegisterUserMutationInput!) {
  register_user(input: $data) {
    user {
      email
      is_staff
      date_joined
    }
    errors {
      field
      messages
    }
  }
}
`;

export const CONFIRM_EMAIL = gql`mutation confirm_email($data: ConfirmEmailMutationInput!) {
  confirm_email(input: $data) {
    success
  }
}
`;

export const REQUEST_EMAIL_CHANGE = gql`mutation request_email_change($data: RequestEmailChangeMutationInput!) {
  request_email_change(input: $data) {
    errors {
      field
      messages
    }
  }
}
`;

export const CONFIRM_EMAIL_CHANGE = gql`mutation confirm_email_change($data: ConfirmEmailChangeMutationInput!) {
  confirm_email_change(input: $data) {
    user {
      email
    }
    errors {
      field
      messages
    }
  }
}
`;

export const REQUEST_PASSWORD_RESET = gql`mutation request_password_reset($data: RequestPasswordResetMutationInput!) {
  request_password_reset(input: $data) {
    errors {
      field
      messages
    }
  }
}
`;

export const CONFIRM_PASSWORD_RESET = gql`mutation confirm_password_reset($data: ConfirmPasswordResetMutationInput!) {
  confirm_password_reset(input: $data) {
    errors {
      field
      messages
    }
  }
}
`;

export const GET_EVENT = gql`query get_event($id: String!) {
  event(id: $id) {
    id
    type
    data
    test_mode
    pending_webhooks
    created_at
  }
}
`;

export const GET_EVENTS = gql`query get_events($filter: EventFilter) {
  events(filter: $filter) {
    page_info {
      has_next_page
      has_previous_page
      start_cursor
      end_cursor
    }
    edges {
      node {
        id
        type
        data
        test_mode
        pending_webhooks
        created_at
      }
    }
  }
}
`;

export const GET_ORDER = gql`query get_order($id: String!) {
  order(id: $id) {
    id
    order_id
    source
    status
    shipping_to {
      id
      postal_code
      city
      person_name
      company_name
      country_code
      email
      phone_number
      state_code
      suburb
      residential
      street_number
      address_line1
      address_line2
      federal_tax_id
      state_tax_id
      validate_location
    }
    shipping_from {
      id
      postal_code
      city
      person_name
      company_name
      country_code
      email
      phone_number
      state_code
      suburb
      residential
      street_number
      address_line1
      address_line2
      federal_tax_id
      state_tax_id
      validate_location
    }
    billing_address {
      id
      postal_code
      city
      person_name
      company_name
      country_code
      email
      phone_number
      state_code
      suburb
      residential
      street_number
      address_line1
      address_line2
      federal_tax_id
      state_tax_id
      validate_location
    }
    line_items {
      id
      weight
      title
      description
      quantity
      unfulfilled_quantity
      sku
      hs_code
      value_amount
      weight_unit
      value_currency
      origin_country
      metadata
      parent_id
    }
    created_at
    updated_at
    created_by {
      email
      full_name
    }
    test_mode
    options
    metadata
    shipments {
      id
      carrier_id
      carrier_name
      created_at
      updated_at
      created_by {
        email
        full_name
      }
      status
      recipient {
        id
        postal_code
        city
        person_name
        company_name
        country_code
        email
        phone_number
        state_code
        suburb
        residential
        street_number
        address_line1
        address_line2
        federal_tax_id
        state_tax_id
        validate_location
      }
      shipper {
        id
        postal_code
        city
        person_name
        company_name
        country_code
        email
        phone_number
        state_code
        suburb
        residential
        street_number
        address_line1
        address_line2
        federal_tax_id
        state_tax_id
        validate_location
      }
      billing_address {
        id
        postal_code
        city
        person_name
        company_name
        country_code
        email
        phone_number
        state_code
        suburb
        residential
        street_number
        address_line1
        address_line2
        federal_tax_id
        state_tax_id
        validate_location
      }
      parcels {
        id
        width
        height
        length
        is_document
        dimension_unit
        weight
        weight_unit
        packaging_type
        package_preset
        freight_class
        reference_number
        items {
          id
          weight
          title
          description
          quantity
          sku
          hs_code
          value_amount
          weight_unit
          value_currency
          origin_country
          metadata
          parent_id
        }
      }
      label_type
      tracking_number
      shipment_identifier
      label_url
      invoice_url
      tracking_url
      test_mode
      service
      reference
      customs {
        id
        certify
        commercial_invoice
        content_type
        content_description
        incoterm
        invoice
        invoice_date
        signer
        duty {
          paid_by
          currency
          account_number
          declared_value
        }
        options
        commodities {
          id
          weight
          weight_unit
          title
          description
          quantity
          sku
          hs_code
          value_amount
          value_currency
          origin_country
          metadata
          parent_id
        }
        duty_billing_address {
          id
          postal_code
          city
          person_name
          company_name
          country_code
          email
          phone_number
          state_code
          suburb
          residential
          street_number
          address_line1
          address_line2
          federal_tax_id
          state_tax_id
          validate_location
        }
      }
      payment {
        paid_by
        currency
        account_number
      }
      selected_rate_id
      selected_rate {
        id
        carrier_name
        carrier_id
        currency
        service
        transit_days
        total_charge
        extra_charges {
          name
          amount
          currency
        }
        test_mode
        meta
      }
      carrier_ids
      rates {
        id
        carrier_name
        carrier_id
        currency
        service
        transit_days
        total_charge
        extra_charges {
          name
          amount
          currency
        }
        test_mode
        meta
      }
      metadata
      meta
      messages {
        carrier_name
        carrier_id
        message
        code
        details
      }
    }
  }
}
`;

export const GET_ORDERS = gql`query get_orders($filter: OrderFilter) {
  orders(filter: $filter) {
    page_info {
      has_next_page
      has_previous_page
      start_cursor
      end_cursor
    }
    edges {
      node {
        id
        order_id
        source
        status
        shipping_to {
          id
          postal_code
          city
          person_name
          company_name
          country_code
          email
          phone_number
          state_code
          suburb
          residential
          street_number
          address_line1
          address_line2
          federal_tax_id
          state_tax_id
          validate_location
        }
        shipping_from {
          id
          postal_code
          city
          person_name
          company_name
          country_code
          email
          phone_number
          state_code
          suburb
          residential
          street_number
          address_line1
          address_line2
          federal_tax_id
          state_tax_id
          validate_location
        }
        billing_address {
          id
          postal_code
          city
          person_name
          company_name
          country_code
          email
          phone_number
          state_code
          suburb
          residential
          street_number
          address_line1
          address_line2
          federal_tax_id
          state_tax_id
          validate_location
        }
        line_items {
          id
          weight
          title
          description
          quantity
          unfulfilled_quantity
          sku
          hs_code
          value_amount
          weight_unit
          value_currency
          origin_country
          metadata
          parent_id
        }
        created_at
        updated_at
        created_by {
          email
          full_name
        }
        test_mode
        options
        metadata
        shipments {
          id
          carrier_id
          carrier_name
          created_at
          updated_at
          created_by {
            email
            full_name
          }
          status
          recipient {
            id
            postal_code
            city
            person_name
            company_name
            country_code
            email
            phone_number
            state_code
            suburb
            residential
            street_number
            address_line1
            address_line2
            federal_tax_id
            state_tax_id
            validate_location
          }
          shipper {
            id
            postal_code
            city
            person_name
            company_name
            country_code
            email
            phone_number
            state_code
            suburb
            residential
            street_number
            address_line1
            address_line2
            federal_tax_id
            state_tax_id
            validate_location
          }
          billing_address {
            id
            postal_code
            city
            person_name
            company_name
            country_code
            email
            phone_number
            state_code
            suburb
            residential
            street_number
            address_line1
            address_line2
            federal_tax_id
            state_tax_id
            validate_location
          }
          parcels {
            id
            width
            height
            length
            is_document
            dimension_unit
            weight
            weight_unit
            packaging_type
            package_preset
            freight_class
            reference_number
            items {
              id
              weight
              title
              description
              quantity
              sku
              hs_code
              value_amount
              weight_unit
              value_currency
              origin_country
              metadata
              parent_id
            }
          }
          label_type
          tracking_number
          shipment_identifier
          label_url
          invoice_url
          tracking_url
          test_mode
          service
          reference
          customs {
            id
            certify
            commercial_invoice
            content_type
            content_description
            incoterm
            invoice
            invoice_date
            signer
            duty {
              paid_by
              currency
              account_number
              declared_value
            }
            options
            commodities {
              id
              weight
              weight_unit
              title
              description
              quantity
              sku
              hs_code
              value_amount
              value_currency
              origin_country
              metadata
              parent_id
            }
            duty_billing_address {
              id
              postal_code
              city
              person_name
              company_name
              country_code
              email
              phone_number
              state_code
              suburb
              residential
              street_number
              address_line1
              address_line2
              federal_tax_id
              state_tax_id
              validate_location
            }
          }
          payment {
            paid_by
            currency
            account_number
          }
          selected_rate_id
          selected_rate {
            id
            carrier_name
            carrier_id
            currency
            service
            transit_days
            total_charge
            extra_charges {
              name
              amount
              currency
            }
            test_mode
            meta
          }
          carrier_ids
          rates {
            id
            carrier_name
            carrier_id
            currency
            service
            transit_days
            total_charge
            extra_charges {
              name
              amount
              currency
            }
            test_mode
            meta
          }
          metadata
          meta
          messages {
            carrier_name
            carrier_id
            message
            code
            details
          }
        }
      }
    }
  }
}
`;

export const MUTATE_METADATA = gql`mutation mutate_metadata($data: MetadataMutationInput!) {
  mutate_metadata(input: $data) {
    id
    metadata
    errors {
      field
      messages
    }
  }
}
`;

export const GET_DOCUMENT_TEMPLATE = gql`query get_document_template($id: String!) {
  document_template(id: $id) {
    id
    slug
    name
    template
    description
    related_object
    active
    updated_at
  }
}
`;

export const GET_DOCUMENT_TEMPLATES = gql`query get_document_templates($filter: DocumentTemplateFilter) {
  document_templates(filter: $filter) {
    page_info {
      has_next_page
      has_previous_page
      start_cursor
      end_cursor
    }
    edges {
      node {
        id
        slug
        name
        template
        description
        related_object
        active
        updated_at
      }
    }
  }
}
`;

export const CREATE_DOCUMENT_TEMPLATE = gql`mutation create_document_template($data:  CreateDocumentTemplateMutationInput!) {
  create_document_template(input: $data) {
    template {
      id
    }
    errors {
      field
      messages
    }
  }
}
`;

export const UPDATE_DOCUMENT_TEMPLATE = gql`mutation update_document_template($data:  UpdateDocumentTemplateMutationInput!) {
  update_document_template(input: $data) {
    template {
      id
    }
    errors {
      field
      messages
    }
  }
}
`;

export const DELETE_DOCUMENT_TEMPLATE = gql`mutation delete_document_template($data: DeleteMutationInput!) {
  delete_document_template(input: $data) {
    id
  }
}
`;

export const SEARCH_DATA = gql`query search_data($keyword: String) {
  shipment_results: shipments(filter: { keyword: $keyword, offset: 0, first: 10 }) {
    edges {
      node {
        id
        status
        tracking_number
        recipient {
          id
          city
          street_number
          address_line1
          address_line2
          country_code
          postal_code
          person_name
          phone_number
          company_name
          state_code
        }
        created_at
      }
    }
  }
  order_results: orders(filter: { keyword: $keyword, offset: 0, first: 10 }) {
    edges {
      node {
        id
        status
        order_id
        shipping_to {
          id
          city
          street_number
          address_line1
          address_line2
          country_code
          postal_code
          person_name
          phone_number
          company_name
          state_code
        }
        created_at
      }
    }
  }
  trackers_results: trackers(filter: {tracking_number: $keyword, offset: 0, first: 10 }) {
    edges {
      node {
        id
        status
        tracking_number
        created_at
      }
    }
  }
}
`;

export const CREATE_RATE_SHEET = gql`mutation create_rate_sheet($data: CreateRateSheetMutationInput!) {
  create_rate_sheet(input: $data) {
    rate_sheet {
      id
    }
    errors {
      field
      messages
    }
  }
}
`;

export const UPDATE_RATE_SHEET = gql`mutation update_rate_sheet($data: UpdateRateSheetMutationInput!) {
  update_rate_sheet(input: $data) {
    rate_sheet {
      id
    }
    errors {
      field
      messages
    }
  }
}
`;

export const DELETE_RATE_SHEET = gql`mutation delete_rate_sheet($data: DeleteMutationInput!) {
  delete_rate_sheet(input: $data) {
    id
    errors {
      field
      messages
    }
  }
}
`;

export const GET_RATE_SHEET = gql`query get_rate_sheet($id: String!) {
  rate_sheet(id: $id) {
    id
    name
    slug
    carrier_name
    services {
      id
      object_type
      service_name
      service_code
      description
      active
      currency
      transit_days
      transit_time
      max_width
      max_height
      max_length
      dimension_unit
      zones {
        object_type
        label
        rate
        min_weight
        max_weight
        transit_days
      }
    }
    carriers {
      id
      active
      carrier_id
      carrier_name
      display_name
      capabilities
      test_mode
    }
  }
}`;

export const GET_RATE_SHEETS = gql`query get_rate_sheets($filter: RateSheetFilter) {
  rate_sheets(filter: $filter) {
    page_info {
      has_next_page
      has_previous_page
      start_cursor
      end_cursor
    }
    edges {
      node {
        id
        name
        slug
        carrier_name
        services {
          id
          service_name
          service_code
          description
          active
          currency
          transit_days
          transit_time
          max_width
          max_height
          max_length
          dimension_unit
          zones {
            label
            rate
            min_weight
            max_weight
            transit_days
          }
        }
        carriers {
          id
          active
          carrier_id
          carrier_name
          display_name
          capabilities
          test_mode
        }
      }
    }
  }
}`;
