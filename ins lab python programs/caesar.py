import random
def encrypt(text,key):
  res=""
  for i in range(len(text)):
    ch=text[i]
    if(ch.isupper()):
      res+=chr((ord(ch)+key-65)%26+65)
    else:
      res+=chr((ord(ch)+key-97)%26+97)
  return(res)
def decrypt(text,key):
  res=""
  for i in range(len(text)):
    ch=text[i]
    if(ch.isupper()):
      res+=chr((ord(ch)-key-65)%26+65)
    else:
      res+=chr((ord(ch)-key-97)%26+97)
  return res   
text=input()
key=input()
print(text)
print(key)
print(encrypt(text,int(key)))
k=input()
list=[i for i in range(11)]
for i in range(5):
    s=random.choice(list)
    print(s)
    s1=encrypt(k,s)
    print(s1)
    print(decrypt(s1,s))