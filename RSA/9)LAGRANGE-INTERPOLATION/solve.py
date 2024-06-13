import ast
from math import isqrt

with open("output.txt") as f:
    n = ast.literal_eval(f.readline())
    e = ast.literal_eval(f.readline())
    c = ast.literal_eval(f.readline())
    s = ast.literal_eval(f.readline())

phi_n = n - s + 1
d = pow(e, -1, phi_n)
m = pow(c, d, n)

flag = bytes.fromhex(hex(m)[2:])

print(f"{flag = }")
def solve_quadratic_equation(b, c):
    """Solve x^2 + bx + c = 0"""
    D = b**2 - 4 * c
    return -b + isqrt(D) >> 1, -b - isqrt(D) >> 1


p, q = solve_quadratic_equation(-s, n)
assert p > 2 and q > 2 and p * q == n

d = pow(e, -1, (p - 1) * (q - 1))
m = pow(c, d, n)
m = int.to_bytes(m, m.bit_length() + 7 >> 3, byteorder="big")
m = m.decode()
print(m)