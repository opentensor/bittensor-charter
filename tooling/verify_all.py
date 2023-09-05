import json
from binascii import unhexlify
from bittensor import Keypair

charter_file = "charter.txt"

with open("signatures.json", "r") as fh:
    information_dict = json.loads(fh.read())

for hotkey, signer_info in information_dict.items():
    if "signature" not in signer_info.keys():
        raise ValueError(f"No signature found for {signer_info['name']} ({hotkey=})")

    keypair = Keypair(ss58_address=hotkey)
    signature = signer_info["signature"].encode()

    del signer_info["signature"]
    charter = ""
    with open (charter_file, "r") as file:
        charter = file.read()

    if not keypair.verify( data = charter, signature = unhexlify( signature ) ):
        raise ValueError(f"Invalid signature for {signer_info['name']} ({hotkey=})")
