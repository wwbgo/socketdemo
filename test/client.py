#coding=utf-8
__author__ = 'wwb'
'''
client端
长连接，短连接，心跳
'''
import socket
import time
from threading import Thread
host = '192.168.50.175'
port = 8088

# host = 'localhost'
# port = 8083

def async(f):
    def wrapper(*args,**kwargs):
        thr=Thread(target=f,args=args,kwargs=kwargs)
        thr.start()
    return wrapper

@async
def senddata(n):
    while True:
        ticks=str(time.time())
        client.send('[1.{1}]:hello world:{0}\r\n'.format(ticks,n).encode())
        print('[1.{1}]:send data:{0}'.format(ticks,n))
        time.sleep(1) #如果想验证长时间没发数据，SOCKET连接会不会断开，则可以设置时间长一点

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1) #在客户端开启心跳维护
client.connect((host, port))
n=0
while n<10:
    n=n+1
    senddata(n)