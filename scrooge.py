from blockchain import BlockChain
from wallet import Wallet


class Scrooge:
    """
    Central trusted authority of ScroogeCoin.
    In charge of
        - Managing the blockchain
        - Creating Coins
    """

    def __init__(self):
        self.blockchain = BlockChain()
        self.wallet = Wallet()
