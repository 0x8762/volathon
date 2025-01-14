from solathon import Client, PublicKey, Keypair

client = Client("https://api.devnet.solana.com")

account = Keypair().from_private_key('5rQjZzW57YA2AKUp5DV9b1G8PPLut3yGrFuDaeDyUgVJZc9G7LCxxaSK6rixicXCcaeCzL2WWhWpUnt8BmbZBu8H')
pbkey = account.public_key

print(pbkey, client.get_balance(pbkey))
