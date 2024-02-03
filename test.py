import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()  # This loads the environment variables from .env file

sepolia_url = os.getenv('SEPOLIA_RPC_URL')
w3 = Web3(Web3.HTTPProvider(sepolia_url))
print(w3.eth.get_transaction_count('0xff1D7A50A54Eb2EAC0786d4c66D4191243B1D889'))