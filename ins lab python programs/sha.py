import hashlib
import time
import matplotlib.pyplot as plt
x=[]
y=[]
for i in range(3):
	file=input()
	k=time.time()
	f=open(file,"r")
	str=f.read()
	result=hashlib.sha1(str.encode())
	print("The hexahexdecimal equivalent of SHA1 is:")
	print(result.hexdigest())
	f=time.time()
	print(f-k)
	x.append(len(str))
	y.append(f-k)
plt.plot(x, y)   
plt.xlabel('input size') 
plt.ylabel('time') 
plt.title('graph')  
plt.show() 	
