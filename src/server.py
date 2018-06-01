#coding=utf-8
__author__ = 'wwb'
'''
server端
长连接，短连接，心跳
'''
import socket
import threading
import time
import redis

BUF_SIZE = 1024
host = '0.0.0.0'
port = 80


q=threading.RLock()
n=0
instance=0

def async(f):
    def wrapper(*args,**kwargs):
        thr=threading.Thread(target=f,args=args,kwargs=kwargs)
        thr.start()
    return wrapper

@async
def recvdata():
    global instance
    while True:
        try:
            client, address = server.accept()
            print(address)
            q.acquire()
            instance=instance+1
            q.release()
            begin=client.recv(BUF_SIZE)
            print(begin.decode())
            if begin.decode() != 'client is ready to recv.':
                client.send(('please send "client is ready to recv." if client is ready.').encode())
                print ('client is not ready to recv.')
                client.close()
                break

            addr=redisdb0.get(address[0])
            if not addr:
                rd=str(time.time())
                redisdb0.set(address[0],rd)
                client.send(('saved to redis:'+rd).encode())
                print('saved to redis:'+rd)
            else:
                addr=addr.decode()
                client.send(('get cache data from redis:'+addr).encode())
                print('get cache data from redis:'+addr)

            while True: 
                ticks=str(time.time())
                client.send(('now:'+ticks+"\r\n").encode())
                print('now:'+ticks)
                time.sleep(1)
        except Exception as e:
            print(e)
            q.acquire()
            instance=instance-1
            q.release()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(10) #接收的连接数
server.recv_into
redisdb0=redis.Redis(host='192.168.50.250',port=32291,db=0)

while True:
    if n<=instance:
        recvdata()
        n=n+1
    elif n-instance>1:
        n=n-1