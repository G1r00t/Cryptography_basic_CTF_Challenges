import base64

def decode_base64_four_times(base64_string):
    decoded_string = base64.b64decode(base64_string).decode('utf-8')
    
    for _ in range(3):  # Decode three more times
        base64_string = decoded_string
        decoded_string = base64.b64decode(base64_string).decode('utf-8')

    return decoded_string

# Example usage:
base64_input = input("Enter the initial base64 string: ")

result = decode_base64_four_times(base64_input)
print("Decoded string after four iterations:", result)
