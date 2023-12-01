from OnChain import constants as c
from OnChain.on_chain_bot import OnChainBot


async def run_onchain_bots():
    for blockchain in c.RPCS.keys():
        on_chain_bot = OnChainBot(blockchain=blockchain)
        await on_chain_bot.run()