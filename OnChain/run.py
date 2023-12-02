import multiprocessing
import asyncio

from OnChain import constants as c
from OnChain.on_chain_bot import OnChainBot


def start_on_chain_bot(blockchain: str):
    on_chain_bot = OnChainBot(blockchain=blockchain, verbose=True)
    asyncio.run(on_chain_bot.run())


def run_on_chain_bots():
    on_chain_bots_processes = []
    for blockchain in c.RPCS.keys():
        on_chain_bot_process = multiprocessing.Process(target=start_on_chain_bot, args=(blockchain,))
        on_chain_bots_processes.append(on_chain_bot_process)
        on_chain_bot_process.start()