from web3 import Web3, HTTPProvider

rpc_url = "http://localhost:8080"
w3 = Web3(HTTPProvider(rpc_url))
w3.geth.personal.unlockAccount(w3.eth.accounts[0], "base", 0)
w3.eth.defaultAccount = w3.eth.accounts[0]
transaction = {
        'to' : w3.eth.accounts[1],
        'from' : w3.eth.accounts[0],
        'value' : w3.toWei('6','ether'),
        'gas' : 21000,
        'gasPrice' : w3.toWei('40','gwei'),
        'chainId':33,
        #'nonce': w3.eth.getTransactionCount(w3.eth.accounts[0])
        'nonce': 11 
        }
with open('/home/sigmoid/WORK/go-ethereum-yogyeog/localdata/keystore/UTC--2019-12-01T14-27-38.958256228Z--f20a6b14113b1ba8cbdf62592fe403c85afab301') as keyfile:
    encrypted_key = keyfile.read()
    private_key = w3.eth.account.decrypt(encrypted_key,'base')
    signed_tx = w3.eth.account.signTransaction(transaction, private_key)
    print(signed_tx)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(tx_hash)
