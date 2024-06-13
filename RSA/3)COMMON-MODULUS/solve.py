import gmpy2
from Crypto.Util.number import *
#bezout's identity
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
#The function will return GCD of e1 and e2 along with the coefficients of Bezout's Identity a and b respectively.
# Calculates a^{b} mod n when b is negative
def neg_pow(a, b, n):
    assert b < 0
    assert GCD(a, n) == 1
    res = int(gmpy2.invert(a, n))
    res = pow(res, b * (-1), n)
    return res

# e1 --> Public Key exponent used to encrypt message m and get ciphertext c1
# e2 --> Public Key exponent used to encrypt message m and get ciphertext c2
# n --> Modulus
# The following attack works only when m^{GCD(e1, e2)} < n
n=80532460110376032015593217904809007064720214843648843519568623316648395747244333344042221197856011627788380898520914752520772301150084167452069303052429625984407708463833552562515571631395657365091932403220200212736190205966050174306711247431647415255945341744145372244715385306052046926102683323950272445421

c1=24364161676374615320198989930199439978579776135939570207244247493057771544990991576489043667852984049058021298633794138775535777542175333345615909825498252705525862222930996919082500714563968328186394766147499501053679825205451644612558273056179299375617301030281027153744167021009725404910252675170098626714
c2=65131461128747599961343950351004394859888695038208255575643098353678109728262464571074541831390009419282790379085189866190997954052144659747257281640409518906999008763466103151985570478509689053252512073618484635316151924641129097023754110638559106096185307517340674526344221461599200821499956756155758123373
e1 = 71
e2 = 101

def common_modulus(e1, e2, n, c1, c2):
    g, a, b = egcd(e1, e2)
    if a < 0:
        c1 = neg_pow(c1, a, n)
    else:
        c1 = pow(c1, a, n)
    if b < 0:
        c2 = neg_pow(c2, b, n)
    else:
        c2 = pow(c2, b, n)
    ct = c1 * c2 % n
    m = int(gmpy2.iroot(ct, g)[0])
    return long_to_bytes(m)

# Call the common_modulus function and print the decrypted message
decrypted_message = common_modulus(e1, e2, n, c1, c2)
print(decrypted_message)