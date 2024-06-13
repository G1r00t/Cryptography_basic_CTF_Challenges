from Crypto.Util.number import *
msg=b'hackersprey{REDACTED}'
pt=bytes_to_long(msg)
e=65537
N=p*q
ct=pow(pt,e,N)
print(N)
print(e)
print(ct)