import { useCarrierConnections } from "./user-connection";
import React from 'react';

export function useConnections() {
  const [carrierOptions, setCarrierOptions] = React.useState<string[]>([]);
  const { query: { data: { user_connections = [] } = {}, ...query } } = useCarrierConnections();

  React.useEffect(() => {
    if (!query.isFetched) { return; }

    const _options: string[][] = (user_connections || []).map(
      (_: any) => (_.active ? _.config?.shipping_options || [] : []) as string[],
      [],
    );

    setCarrierOptions(([] as string[]).concat(..._options));
  }, [user_connections, query.isFetched]);

  return {
    carrierOptions
  };
}
