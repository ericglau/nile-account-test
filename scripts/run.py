
from nile.core.account import Account

async def run(nre):
    signer = "PRIVATE_KEY"
    await Account(signer, nre.network, watch_mode="track")
