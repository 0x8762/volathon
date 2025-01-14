from solathon.core.instructions import transfer
from solathon import Client, Transaction, PublicKey, Keypair


def lamport_to_sol(lamp):
    return lamp / 1000000000 

def sol_to_lamport(sol):
    return sol * 1000000000 

client = Client("https://api.devnet.solana.com")

new_account = Keypair().from_private_key("4rgXz3CkUkDmRwUjR4uW66qmsqw6576rbJZxtwVUuPdFscwh63Xzh58Sbx1sHwJDtnujfdZf3NjFWJvvP2AnxiNS")
print("gros compte", lamport_to_sol(client.get_balance(new_account.public_key)))

noan = Keypair().from_private_key("5rQjZzW57YA2AKUp5DV9b1G8PPLut3yGrFuDaeDyUgVJZc9G7LCxxaSK6rixicXCcaeCzL2WWhWpUnt8BmbZBu8H")

print("petit compte", lamport_to_sol(client.get_balance(noan.public_key)))


def send(toto):
    sender = new_account
    receiver = PublicKey("4PoTcps9heW7xYzMLza841PqrZ7C7TgFVyHQsY3fYSv9")
    amount = 300000000 # This is the amount in lamports

    instruction = transfer(
        from_public_key=sender.public_key,
        to_public_key=receiver, 
        lamports=amount
    )
    transaction = Transaction(instructions=[instruction], signers=[sender])

    result = client.send_transaction(transaction)
    print(result)

#send("‌4PoTcps9heW7xYzMLza841PqrZ7C7TgFVyHQsY3fYSv9")
print(new_account.private_key)