def xor_decrypt(ciphertext, key):
    return ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(ciphertext, key))

encrypted_message = "encrypted_message_here"
xor_key = "random_xor_key"

decrypted_flag = xor_decrypt(encrypted_message, xor_key)
print(decrypted_flag)