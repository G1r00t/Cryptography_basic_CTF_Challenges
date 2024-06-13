#Given the string 'alarm', XOR each character with the integer 29. Convert these integers back to a string and submit the flag as crypto{new_string}.
string = "J~tsndfkWfssbuiX573"
integer = 7

unicode_repr = [ord(c) for c in string]
xor_unicode = [7 ^ i for i in unicode_repr] # xor : ^
flag = "".join(chr(o) for o in xor_unicode)
print(flag)
#R3s3c{fkfuj}
# def xor_strings(input_string, key):
#     result = ""
#     for i in range(len(input_string)):
#         result += chr(ord(input_string[i]) ^ key[i % len(key)])
#     return result

# # The target string is "MysticalPattern_204"
# target_string = "MysticalPattern_204"

# # Choose a key with the same length as the target string
# key = [ord(target_string[i]) for i in range(len(target_string))]

# # XOR the key with a number of your choice
# your_number = 7  # You can replace this with any number you like

# result_string = xor_strings(target_string, [your_number] * len(target_string))

# print(f"Input String: {result_string}")
# print(f"XOR with {your_number}: {xor_strings(result_string, key)}")
