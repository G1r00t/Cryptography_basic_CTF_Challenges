from Crypto.Util.number import *
n=166045890368446099470756111654736772731460671003059151938763854196360081247044441029824134260263654537
e=65537
msg=bytes_to_long(b'hackersprey{REDACTED}')
ct=pow(msg,e,n)
print(n)
print(e)
print(ct)   
