import bittensor
from bittensor import Keypair
import json

charter_file = "./charter.txt"
output_file = "./signatures.json"

name = input("Your entity's descriptive name (e.g. Opentensor Foundation):\n")
url = input("Your validator url (e.g. www.opentensor.org ) [Optional]:\n")
mnemonic = input(
    "The mnemonic of your validator's hotkey "
    "( default location: ~/.bittensor/wallets/<coldkey>/hotkeys/<validator> )\n"
)

keypair = Keypair.create_from_mnemonic(mnemonic)
signature_entry = dict()
signature_entry[keypair.ss58_address] = {
    "name": name,
    "url": url,
}


def sign_charter(keypair):

    # First load the charter text file
    charter = ""
    with open (charter_file, "r") as file:
        charter = file.read()
    
    # Now sign it with wallet hotkey
    signature = keypair.sign(charter)
    signature_entry[keypair.ss58_address]["signature"] = signature.hex()

    if keypair.verify(charter, signature):
        with open(output_file, "r") as file:
            signatures = json.loads(file.read())
        signatures.update(signature_entry)

        with open(output_file, "w") as file:
            file.write(json.dumps(signatures, indent=4, ensure_ascii=False))
        return signature_entry
    
    return None


# Load the wallet using the supplied 
signature = sign_charter(keypair)
if signature:



    print("Signature: \n {}. Saved in file {}".format(signature, output_file))