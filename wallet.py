from solathon import Client, PublicKey, Keypair, Transaction
from solathon.core.instructions import transfer

client = Client("https://api.devnet.solana.com")

def get_account_from_key(private_key:str)->Keypair:
    return Keypair().from_private_key(private_key)

def send(sender:Keypair, receiver:PublicKey, amount:int):
    instruction = transfer(
        from_public_key=sender.public_key,
        to_public_key=receiver, 
        lamports=amount
    )
    transaction = Transaction(instructions=[instruction], signers=[sender])

    return client.send_transaction(transaction)

account = Keypair().from_private_key('5rQjZzW57YA2AKUp5DV9b1G8PPLut3yGrFuDaeDyUgVJZc9G7LCxxaSK6rixicXCcaeCzL2WWhWpUnt8BmbZBu8H')
pbkey = account.public_key

print(pbkey, client.get_balance(pbkey))