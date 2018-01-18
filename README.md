# ScroogeCoin
ScroogeCoin is a centralized crypto-currency, defined in the textbook "Bitcoin and Cryptocurrency Technologies" (Princeton University)

## Specifications of the currency
#### Coin Creation**
- Scrooge is the central actor in this currency, as the trusted central entity he is in charge of minting new coins and appending new blocks to the blockchain.

#### Transaction Types in the Blockchain
1. **CreateCoins**
  * Only Scrooge can create one of these
  * Multiple coins allowed to be created
  * Each coin has a recipient
  * Each coin created is uniquely identified by a *CoinID*, a combination of the transaction ID, and the coin serial number

2. **PayCoins**
  * Consumes coins (destroys them) and creates new coins of the same total value
  * Coins consumed must be valid (i.e. created in a previous transaction)
  * No double-spending
  * Total value of coins that come in must be the same going out (i.e. CreateCoins is the only way new coins are created)
  * Any participant spending must digitally sign the transaction

#### Hashing and Signing
  * *sha256* for hashing
  * *ecdsa* for signing

