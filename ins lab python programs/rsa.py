import random
import math
def isprime(x):
  if(x<2):
    return False
  else:
    for n in range(2,x):
      if(x%n==0):
        return False
  return True
primes=[i for i in range(10,100) if(isprime(i))]
p=random.choice(primes)
primes.remove(p)
q=random.choice(primes)      
print(p)
print(q)
n=p*q
phi=(p-1)*(q-1)
z=int(input())
for i in range(2,phi):
  if(math.gcd(i,phi)==1):
    e=i
    break
d=1
while(True):
  if((e*d)%phi==1):
    D=d
    break
  d=d+1
print("public key is:",e)
print("private key is:",D)
en=pow(z,e)%n
print("encrypted:",en)
decrypt=pow(en,D)%n
print("decrypted:",decrypt)