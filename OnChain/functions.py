from typing import Union
import os

def add_unit_to_bignumber(bignumber: Union[int, float]):

        bignumber = float(bignumber)
        units = ["", "K", "M", "B", "T", "Q", "Qi", "Sx", "Sp", "O", "N", "D"]
        unit_index = 0

        while bignumber >= 1000:
                bignumber /= 1000.0
                unit_index += 1

        formatted_number = "{:.2f}{}".format(bignumber, units[unit_index])
        return formatted_number


def load_wallets(blockchain: str):
        with open(os.path.join(os.getcwd(), 'wallets.txt'), 'r') as wallets_file:
                wallets = [line.strip() for line in wallets_file.readlines() if line.startswith(blockchain)]
                blockchain_wallets = []
                for wallet in wallets:
                        blockchain_wallets.append(wallet.replace(f"{blockchain}:", ""))
        return blockchain_wallets