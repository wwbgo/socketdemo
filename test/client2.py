#coding=utf-8
__author__ = 'wwb'
'''
client端
长连接，短连接，心跳
'''
import socket
import time

host = '192.168.50.196'#'192.168.50.250'
port = 80
BUF_SIZE = 1024

def socketconn():
    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    cli.connect((host, port))
    return cli

client= socketconn()
while True:
    try:
        client.send(('client is ready to recv.').encode())
        print('client is ready to recv.')
        while True:
            data=client.recv(BUF_SIZE)
            if not data:
                break
            print(data.decode())
    except Exception as e:
        print(e)
        time.sleep(5)
        client= socketconn()
