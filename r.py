import math

def gcd(a, h):
    while h != 0:
        a, h = h, a % h
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

p = int(input("Enter the first prime number (p): "))
q = int(input("Enter the second prime number (q): "))
msg = int(input("Enter the message to encrypt (as a number): "))

n = p * q
e = 2
phi = (p - 1) * (q - 1)

while e < phi:
    if gcd(e, phi) == 1:
        break
    else:
        e += 1

d = mod_inverse(e, phi)

print("Message data =", msg)

c = pow(msg, e, n)
print("Encrypted data =", c)

m = pow(c, d, n)
print("Original Message Sent =", m)
