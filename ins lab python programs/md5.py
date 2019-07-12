import hashlib
import time
import matplotlib.pyplot as plt
x=[]
y=[]
for i in range(4):
	k=time.time()
	data=input()
	result=hashlib.md5(data.encode())
	print("the hexadecimal equivalent is: ",end="")
	print(result.hexdigest())
	f=time.time()
	print(f-k)
	x.append(len(data))
	y.append(f-k)
plt.plot(x,y)
plt.xlabel('input size')
plt.ylabel('time')
plt.title('graph')
plt.show()