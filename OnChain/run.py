import multiprocessing
import asyncio

from OnChain import constants as c
from OnChain.on_chain_bot import OnChainBot


def start_on_chain_bot(blockchain: str):
    """
    Starts the on chain bot from the blockchain specified.
    
    Parameters:
        ``blockchain (str)``: name of the blockchain, e.g. ETHEREUM
    """
    on_chain_bot = OnChainBot(blockchain=blockchain, verbose=True)
    asyncio.run(on_chain_bot.run())


def run_on_chain_bots():
    """
    Creates a proccess for each on chain bot where a RPC exists for it in OnChain/constants.py.
    """
    on_chain_bots_processes = []
    for blockchain in c.RPCS.keys():
        on_chain_bot_process = multiprocessing.Process(target=start_on_chain_bot, args=(blockchain,))
        on_chain_bots_processes.append(on_chain_bot_process)
        on_chain_bot_process.start()