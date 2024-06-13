def number_to_character(num):
    if 0 <= num < 26:
        return chr(num + ord('a'))
    elif 26 <= num < 36:
        return str(num - 26)
    elif num == 36:
        return '_'
    else:
        raise ValueError("Invalid number")
# % : mod 18 % 5 = 3
numbers = [279 ,124, 381, 495, 39, 121, 197, 357, 425, 19, 152, 313, 653 ,73, 102, 359, 772]

flag = ''.join([number_to_character(num % 37) for num in numbers])

print(flag)

