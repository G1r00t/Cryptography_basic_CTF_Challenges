from functools import reduce

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n,a):
        p = prod/n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
    
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0,1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a , b = b, a%b
        x0, x1 = x1 -q*x0, x0
    if x1 < 0:
        x1 += b0
    return x1

a = [2,7,9] # x = a mod x
n = [3,13,19] # x = x mod n
#332 

print(chinese_remainder(n,a))
# x = a1 inv (p , n1 )
# case of two integers
# x = a1 mod n1
# x = a2 Mod n2 
# bezouts identity 
# m1n1 + m2n2 =1 
# x = a1m2n2 + a2m1n1
# x = a(1-m1n1) + a2m1n1 
#   = a1 + (a2-a1)m1n1 
# x  = a1 mod n1