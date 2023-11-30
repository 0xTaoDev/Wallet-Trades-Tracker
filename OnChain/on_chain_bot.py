import asyncio

from web3 import Web3
from web3.exceptions import BlockNotFound
from web3_multi_provider import MultiProvider
from multicall import Call, Multicall


from OnChain import constants as c
from OnChain import functions as f


class OnChainBot():
    
    def __init__(self, blockchain: str):
        self.blockchain = blockchain
        self.web3 = Web3(MultiProvider(c.RPCS[blockchain]))
        self.block_number = self.get_block_number()
        
    def get_block_number(self):
        return self.web3.eth.get_block_number()
    
    def get_block_transactions(self):
        while True:
            try:
                block = self.web3.eth.get_block(self.block_number, full_transactions=True)
                transactions = block['transactions']
                return transactions
            # If RPC provider not synchronized
            except BlockNotFound:
                pass
    
    async def process_transactions(self):
        wallets = ["0xae2fc483527b8ef99eb5d9b44875f005ba1fae13"]
        filtered_transactions = [
            transaction for transaction in self.transactions
            if transaction.get('from', '').lower() not in [wallet.lower() for wallet in wallets]
        ]
        swaps_transactions_to_process = [asyncio.create_task(self.process_swaps_transactions(transaction=transaction)) for transaction in filtered_transactions]
        await asyncio.gather(*swaps_transactions_to_process)
        
    async def process_swaps_transactions(self, transaction):
        tx_infos = self.web3.eth.get_transaction_receipt(transaction.hash.hex())
        from_address = transaction['from']
        tx_logs = tx_infos['logs']
        
        if tx_infos['status'] == 1:
            for tx_log in tx_logs:
                for tx_log_topic in tx_log['topics']:
                    for pool_type, pool_values in c.SWAPS_HEX[self.blockchain].items():
                        if any(tx_log_topic in hex_value for hex_value in pool_values):
                            swap_data = tx_log['data'][2:]
                            
                            pool_address = tx_log['address']
                            
                            # Token0 & Token1 addresses
                            queries = [
                            Call(pool_address, 'token0()(address)', [['token0_address', None]]),
                            Call(pool_address, 'token1()(address)', [['token1_address', None]])
                            ]
                            tokens_addresses = await Multicall(queries, _w3=self.web3, require_success=True).coroutine()
                            token0_address = Web3.toChecksumAddress(tokens_addresses['token0_address'])
                            token1_address = Web3.toChecksumAddress(tokens_addresses['token1_address'])
                            
                            # Token0 & Token1 decimals & symbols
                            queries = [
                            Call(token0_address, 'decimals()(uint8)', [['token0_decimals', None]]),
                            Call(token1_address, 'decimals()(uint8)', [['token1_decimals', None]]),
                            Call(token0_address, 'symbol()(string)', [['token0_name', None]]),
                            Call(token1_address, 'symbol()(string)', [['token1_name', None]])
                            ]
                            tokens_info = await Multicall(queries, _w3=self.web3, require_success=True).coroutine()
                            decimals_token0 = tokens_info['token0_decimals']
                            decimals_token1 = tokens_info['token1_decimals']
                            
                            print(pool_address, token0_address, token1_address)

                            if pool_type == "V2_POOL":
                                pass
                            elif pool_type == "V3_POOL":
                                pass
             
    async def run(self):
        latest_block_number = self.get_block_number()
        
        while True:
            current_block_number = self.get_block_number()
            
            if current_block_number > latest_block_number:
                print(current_block_number)
                latest_block_number = current_block_number
                self.block_number = current_block_number
                self.transactions = self.get_block_transactions()
                await self.process_transactions()
   
        
async def run_onchain_bots():
    for blockchain in c.RPCS.keys():
        on_chain_bot = OnChainBot(blockchain=blockchain)
        await on_chain_bot.run()
     
        
if __name__ == '__main__':
    asyncio.run(run_onchain_bots())