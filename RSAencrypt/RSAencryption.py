from Crypto.Util.number import getPrime, isPrime, bytes_to_long
import random

flag = b"RHUL(p_and_q)"

p = getPrime(256)

delta = random.randint(1, 2**16)
q = p + delta

while not isPrime(q):
    q += 1

n = p * q
e = 65537

m = bytes_to_long(flag)
ciphertext = pow(m, e, n)

print("n =", n)
print("e =", e)
print("ciphertext =", ciphertext)