import multiprocessing
import asyncio

from OnChain import constants as c
from OnChain.on_chain_bot import OnChainBot


def start_on_chain_bot(blockchain):
    bot = OnChainBot(blockchain=blockchain, verbose=False)
    asyncio.run(bot.run())


async def run_on_chain_bots():
    processes = []
    for blockchain in c.RPCS.keys():
        process = multiprocessing.Process(target=start_on_chain_bot, args=(blockchain,))
        processes.append(process)
        process.start()