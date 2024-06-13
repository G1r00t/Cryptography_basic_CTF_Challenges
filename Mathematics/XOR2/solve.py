encrypted = b'09;3=*+(*=!-""4=	-=+,jhm%'

for char in range(256):
    key = chr(char)
    decrypted = ''.join([chr(x ^ ord(key)) for x in encrypted])
    if all(31 < ord(c) < 127 or c in '\n\r\t' for c in decrypted):
        print(f"Key found: {key}\nDecrypted message: {decrypted}")
#R3S3C(CAPTURE_THE_FLAG)
# def xor_strings(input_string, key):
#     result = ""
#     for i in range(len(input_string)):
#         result += chr(ord(input_string[i]) ^ ord(key))
#     return result

# # The target string is "PuzzleQuest_205"
# target_string = "hackersprey{PuzzleQuest_205}"

# # Choose a key, a single English alphabet letter
# your_key = 'H'  # You can replace this with any letter

# result_string = xor_strings(target_string, your_key)

# print(f"Input String: {result_string}")
# print(f"XOR with '{your_key}': {xor_strings(result_string, your_key)}")
