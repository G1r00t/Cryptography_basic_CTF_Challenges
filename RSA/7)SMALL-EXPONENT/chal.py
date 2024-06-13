from Crypto.Util.number import *
msg=b"hackersprey{REDACTED}"
pt=bytes_to_long(msg)
p=getPrime(1024)
q=getPrime(1024)
N=p*q
e=3
ct=pow(pt,e,N)

print(N)
print(e)
print(ct)