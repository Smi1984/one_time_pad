#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os

from itertools import cycle        
from binascii import unhexlify, hexlify

def xor(s1, s2):     # xor two strings of different lengths
    return hexlify(''.join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(unhexlify(s1), cycle(unhexlify(s2)))))


list = ["The secret message is: When using a stream cipher, never use the key more than once"]
list2 =["We can factor the number 15 with quantum computers. We can also factor the number 15 with a dog trained to bark three times."]
   


c1 = "315c4eeaa8b5f8aaf9174145bf43e1784b8fa00dc71d885a804e5ee9fa40b16349c146fb778cdf2d3aff021dfff5b403b510d0d0455468aeb98622b137dae857553ccd8883a7bc37520e06e515d22c954eba5025b8cc57ee59418ce7dc6bc41556bdb36bbca3e8774301fbcaa3b83b220809560987815f65286764703de0f3d524400a19b159610b11ef3e"
c2 = "234c02ecbbfbafa3ed18510abd11fa724fcda2018a1a8342cf064bbde548b12b07df44ba7191d9606ef4081ffde5ad46a5069d9f7f543bedb9c861bf29c7e205132eda9382b0bc2c5c4b45f919cf3a9f1cb74151f6d551f4480c82b2cb24cc5b028aa76eb7b4ab24171ab3cdadb8356f"
ct = "32510ba9babebbbefd001547a810e67149caee11d945cd7fc81a05e9f85aac650e9052ba6a8cd8257bf14d13e6f0a803b54fde9e77472dbff89d71b57bddef121336cb85ccb8f3315f4b52e301d16e9f52f904"
r = xor(c1,ct)
#a = "because".encode("hex")

print r

os.system('cls' if os.name == 'nt' else 'clear')
i=0
f = open("data2.txt", "wb")
for a in list:
	print "String a  : " + a
	a = a.encode("hex")
	i=i+1
	
	print "String a  : " + a + " i : ",i
	mes = xor(r,a)
	res = mes.decode("hex")
	print "String mes: " + res
	f.write(res)      # str() converts to string
	

