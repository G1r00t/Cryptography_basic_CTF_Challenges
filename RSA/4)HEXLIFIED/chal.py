from Crypto.Util.number import *
msg = b'hackersprey{REDACTED}'
m = bytes_to_long(msg)
n = p*q
e = 65537
c = pow(m,e,n)
print(hex(n))
print(hex(c))
print(hex(e))

