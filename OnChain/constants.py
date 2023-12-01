from hexbytes import HexBytes

from OnChain import functions as f


RPCS = {
    "ETHEREUM": [
        "https://eth.llamarpc.com",
        "https://rpc.ankr.com/eth",
        "https://rpc.mevblocker.io",
        "https://rpc.flashbots.net"
    ]
}

SWAPS_HEX = {
    "ETHEREUM": {
        "V2_POOL": [
            HexBytes('0xc685db7ecb946f6dd83d43ee07d73ec25761abdc54bc77317d0b810b75ce42a9'),
            HexBytes('0xd78ad95fa46c994b6551d0da85fc275fe613ce37657fb8d5e3d130840159d822')
        ],
        "V3_POOL": [
            HexBytes('0xc42079f94a6350d7e6235f29174924f928cc2ac818eb64fed8004e115fbcca67')
        ]
    }
}

LINKS = {
    "SCANS": {
        "ETHEREUM": {
            "MAKER": "https://etherscan.io/address/",
            "TRANSACTION": "https://etherscan.io/tx/",
            "TOKEN": "https://etherscan.io/token/"
        }
    },
    "CHARTS": {
        "ETHEREUM": {
            "DEXSCREENER": "https://dexscreener.com/ethereum/"
        }
    }
}