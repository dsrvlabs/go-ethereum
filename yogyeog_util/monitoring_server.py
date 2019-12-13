#!/usr/bin/env python3

import _thread
import socket
from web3 import Web3, HTTPProvider

HOST = '0.0.0.0'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


def on_new_client(conn,addr):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print('Received', repr(data))

                # if registered address & large amount
                # send raw tx
    #            rpc_url = "http://localhost:8080"
    #            w3 = Web3(HTTPProvider(rpc_url))
    #            tx_hash = w3.eth.sendRawTransaction("0xf86d128509502f9000825208949aea291a1914035830044d06fc4a8b398e59b4cf8904e1003b28d92800008066a0aebbca57b530571a4951a6cd06804eb488a841ef9ffe1fccfa778fae2a50817ca005237703c770e25efebec6f089eb6b93c5b7a220bd4f801b71a6e4a1695d7469")
    conn.close()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        print('Connected by', addr)
        _thread.start_new_thread(on_new_client,(conn,addr))
    s.close()
