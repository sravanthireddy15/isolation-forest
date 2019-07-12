import time
import matplotlib.pyplot as pyplot
from pyDes import pyDes

key="sravs"
data=input()
k=pyDes.des(key,pyDes.CBC,"0/0/0/0/0/0/0/0",pad=none,padmode=pyDes.PAD_PKCS5)
en=k.encrypt(data)
print("encrypted:",en)
print(k.decrypt(en))