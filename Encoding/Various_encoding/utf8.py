utf8_bytes = b'\x50\x61\x73\x73\x77\x6F\x72\x64\x31\x32\x33'

utf8_string = utf8_bytes.decode('utf-8')

print(utf8_string)
from Crypto.Util.number import long_to_bytes
print(long_to_bytes(113583544873929443283674045461665115493))
