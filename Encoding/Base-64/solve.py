import base64

base64_encoded_string = 'UjNzM2N7QmFzZTY0XzFzX2wwdjN9'

base64_decoded = base64.b64decode(base64_encoded_string)

print(base64_decoded)
