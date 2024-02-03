import os
import json
from dotenv import load_dotenv
from web3 import Web3

load_dotenv()  # This loads the environment variables from .env file

# Connect fo Sepolia testnet
sepolia_url = os.getenv('SEPOLIA_RPC_URL')
w3 = Web3(Web3.HTTPProvider(sepolia_url))

# alternative connection check by checking and returning the latest block number
try:
    latest_block = w3.eth.block_number
    print(f"Successfully connected to Sepolia. Latest block: {latest_block}")
except Exception as e:
    print("Failed to connect to the Ethereum network.", e)

# load contract's ABI
with open('feedback_abi.json', 'r') as abi_definition:
    contract_abi = json.load(abi_definition)

contract_address = '0x8B1213b5Abbca9b7a800d9076F1f27d1b91a5bAD'

# Load the contract
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# This function creates a transaction, signs it with the user's private key and sends it to the contract
# Note that private key handling should change to client side (i.e Metamask) for security in further development
# Also need to add: error handling for txn sending and receipt (out-of-gas errors, reverted txns or network connectivity issues)

def submit_feedback(feedback_message, user_address, user_private_key):
    # Ensure correct nonce is used
    nonce = w3.eth.get_transaction_count(user_address)

    # Build the transaction
    tx = {
        'to': contract_address,
        'value': 0,
        'gas': 2000000,
        'gasPrice': Web3.to_wei('10', 'gwei'),
        'nonce': nonce,
        'data': contract.encodeABI(fn_name='submitFeedback', args=[feedback_message]),
        'chainId': 11155111,
    }

    # Sign the transaction with the user's private key
    signed_tx = w3.eth.account.sign_transaction(tx, private_key = user_private_key)
    
    # Send the transaction
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    
    # Wait for the transaction receipt
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    print(f"Transaction receipt: {receipt}")
    return receipt

if __name__ == "__main__":
    feedback = "This is a test feedback message"
    user_address = "0xff1D7A50A54Eb2EAC0786d4c66D4191243B1D889"  # public key
    private_key = os.getenv('PRIVATE_KEY')  
    receipt = submit_feedback(feedback, user_address, private_key)
    print(f"Transaction successful with hash: {receipt.transactionHash.hex()}")
