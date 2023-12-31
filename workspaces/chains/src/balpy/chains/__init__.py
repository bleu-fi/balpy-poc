from enum import Enum


class Chain(Enum):
    mainnet = 1
    polygon = 137
    polygon_zkevm = 1101
    arbitrum = 42161
    gnosis = 100
    optimism = 10
    avalanche = 43114
    goerli = 5
    sepolia = 11155111
    base = 8453
    bsc = 56
    fantom = 250

    def __init__(self, id) -> None:
        self.id = id


ALL_CHAINS = [chain for chain in Chain]

CHAIN_NAMES = {
    Chain.mainnet: "ethereum",
    Chain.polygon: "polygon",
    Chain.polygon_zkevm: "zkevm",
    Chain.arbitrum: "arbitrum",
    Chain.gnosis: "gnosis",
    Chain.optimism: "optimism",
    Chain.avalanche: "avalanche",
    Chain.goerli: "goerli",
    Chain.sepolia: "sepolia",
    Chain.base: "base",
    Chain.bsc: "bsc",
    Chain.fantom: "fantom",
}

CHAIN_SCANNER_MAP = {
    Chain.mainnet: "https://etherscan.io",
    Chain.polygon: "https://polygonscan.com",
    Chain.polygon_zkevm: "https://zkevm.polygonscan.com/",
    Chain.arbitrum: "https://arbiscan.io",
    Chain.gnosis: "https://gnosisscan.io",
    Chain.optimism: "https://optimistic.etherscan.io",
    Chain.avalanche: "https://snowtrace.io/",
    Chain.goerli: "https://goerli.etherscan.io/",
    Chain.sepolia: "https://sepolia.etherscan.io/",
    Chain.base: "https://basescan.org/",
    Chain.bsc: "https://bscscan.com",
    Chain.fantom: "https://ftmscan.com",
}
