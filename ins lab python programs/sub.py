def encrypt(plaintext,key,alphabet):
	keyindex=[alphabet.index(i) for i in plaintext]
	return "".join(key[k] for k in keyindex)
def decrypt(cipher,key,alphabet):
    keyindex=[key.index(i) for i in cipher]
    return "".join(alphabet[k] for k in keyindex)
alphabet='abcdefghijklmnopqrstuvwxyz!@#$%'
key='ghijklmnopqrstuvwxyzbcdef^&*()'
plaintext=input()
cipher=encrypt(plaintext,key,alphabet)
print(cipher)
print(decrypt(cipher,key,alphabet))
