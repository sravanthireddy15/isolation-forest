from Crypto.Hash import HMAC
secret = 'Swordfish'
h=HMAC.new(secret)
h.update("Hello")
print(h.hexdigest())