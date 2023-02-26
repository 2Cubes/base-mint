from web3 import Web3
import requests
from termcolor import cprint
import time
import json
import random

gasLimit = 124000
gwei = 17

def base(privatekey):

    def mint():

        try:
            RPC = "https://eth-mainnet.g.alchemy.com/v2/m7jct_e0_RFwpmnTcHiOdV8SfWk-288Z"

            web3 = Web3(Web3.HTTPProvider(RPC))
            account = web3.eth.account.privateKeyToAccount(privatekey)
            address_wallet = account.address
            contractToken = Web3.toChecksumAddress('0xD4307E0acD12CF46fD6cf93BC264f5D5D1598792')
            ABI = '[{"inputs":[{"internalType":"address","name":"_logic","type":"address"},{"internalType":"bytes","name":"_data","type":"bytes"}],"stateMutability":"payable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"previousAdmin","type":"address"},{"indexed":false,"internalType":"address","name":"newAdmin","type":"address"}],"name":"AdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"beacon","type":"address"}],"name":"BeaconUpgraded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"implementation","type":"address"}],"name":"Upgraded","type":"event"},{"stateMutability":"payable","type":"fallback"},{"stateMutability":"payable","type":"receive"},{"name": "purchase","type": "function","payable":true,"inputs": [{"type": "uint256"}]}]'
            contract = web3.eth.contract(address=contractToken, abi=ABI)

            nonce = web3.eth.get_transaction_count(address_wallet)

            contract_txn = contract.functions.purchase(1).buildTransaction({
                'from': address_wallet,
                'value': 777000000000000,
                'gas': gasLimit,
                'gasPrice': gwei * 1000000000,
                'nonce': nonce,
            })

            signed_txn = web3.eth.account.sign_transaction(contract_txn, private_key=privatekey)
            tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

            cprint(f'\n>>> https://etherscan.io/tx/{web3.toHex(tx_hash)}', 'green')
        except Exception as error:
            cprint(f'\n>>> {error}', 'red')

    mint()
    time.sleep(random.randint(2,4))

if __name__ == "__main__":

    with open("private_keys.txt", "r") as f:
        keys_list = [row.strip() for row in f]

    for privatekey in keys_list:
        base(privatekey)