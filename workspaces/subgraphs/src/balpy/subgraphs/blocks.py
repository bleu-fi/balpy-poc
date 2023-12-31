# balpy_v2/lib/blocks/subgraph.py
import os

import httpx
from balpy.chains import Chain
from balpy.core.lib.time import get_time_24h_ago, get_timestamps
from balpy.subgraphs.gql import gql

BLOCKS_SUBGRAPH_URL_MAP = {
    Chain.mainnet: "https://api.thegraph.com/subgraphs/name/blocklytics/ethereum-blocks",
    Chain.polygon: "https://api.thegraph.com/subgraphs/name/ianlapham/polygon-blocks",
    # Chain.polygon_zkevm: TODO
    Chain.arbitrum: "https://api.thegraph.com/subgraphs/name/ianlapham/arbitrum-one-blocks",
    # Chain.gnosis: TODO
    # Chain.optimism: TODO
    # Chain.avalanche: TODO
    # Chain.goerli: TODO
    # Chain.sepolia: TODO
    # Chain.base: TODO
}


CHAIN_BLOCK_EXPLORER_FN_MAP = {
    Chain.gnosis: lambda timestamp: f"https://api.gnosisscan.io/api?module=block&action=getblocknobytime&timestamp={timestamp}&closest=before&apikey={os.getenv('GNOSIS_API_KEY')}",
}

BLOCKS_QUERY = """
query($timestamp_gte: BigInt, $timestamp_lt: BigInt) {
	blocks(
        first: 1,
        orderBy: number,
        orderDirection: asc,
        where: {
            timestamp_gte: $timestamp_gte,
            timestamp_lt: $timestamp_lt
        }
      ) {
            number
      }
}
"""


CHAIN_AVG_BLOCK_TIME = {
    Chain.mainnet: 13,
    Chain.polygon: 2,
    Chain.arbitrum: 2,
    Chain.gnosis: 2,
}


async def best_guess(chain=Chain.gnosis, t=get_time_24h_ago()) -> int:
    async with httpx.AsyncClient() as client:
        r = await client.get(CHAIN_BLOCK_EXPLORER_FN_MAP[chain](t))

    return int(r.json()["result"])


async def get_block_number_by_timestamp(
    chain=Chain.mainnet, timestamp=get_time_24h_ago()
) -> int:
    url = BLOCKS_SUBGRAPH_URL_MAP.get(chain)

    if not url:
        return await best_guess(chain, timestamp)

    data = await gql(
        BLOCKS_SUBGRAPH_URL_MAP[chain],
        BLOCKS_QUERY,
        variables=get_timestamps(timestamp),
    )
    return int(data["blocks"][0]["number"])
