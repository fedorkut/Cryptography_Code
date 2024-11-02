#key generation, key distribution, encryption, and decryption
#Rivest-Shamir-Adleman
# Example function to compute the gcd (greatest common divisor) 
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
    
# let's calculate some examples using algorithm
n1=gcd(50,10)
n2=gcd(99,33)
n3=gcd(59,9)

# do the same with the python library call
import math
m1=math.gcd(50,10)
m2=math.gcd(99,33)
m3=math.gcd(59,9)

# Confirm they are the same
assert(n1==m1)
assert(n2==m2)
assert(n3==m3)

# They are - print out the values for explanation
print("gcd(50,10) =",m1)
print("gcd(99,1033) =",m2)
print("gcd(59,9) =",m3)

# Choosing two prime numbers and keep them secret
p = 6269
q = 17
print("The secret prime numbers p and q are:", p, q)

# Calculate n which is the modulus for both the public and private keys
n = p * q
print("modulus n (p*q)=",n)

# Compute Euler's totient function, φ(n) and keep it secret
phi = (p-1) * (q-1)
print("The secret Euler's function (totient) [phi(n)]:",phi)

# Choose an integer e such that e and φ(n) are coprime
e = 2
while (e < phi):
    if (math.gcd(e, phi)==1):
        break
    else:
        e += 1
print("Public Key (e):",e)

# Compute a value for d such that (d * e) % φ(n) = 1
d = 1
while(True):
    if((d*e) % phi == 1):
        break
    else:
        d += 1
print("Private Key (d):",d)

# Public and Private Key pair
public = (e, n)
private = (d, n)

print(f"The Public key is {public} and Private Key is {private}")

# Encryption function
def encrypt(plain_text):
    return (plain_text ** e) % n

# Decryption function
def decrypt(cipher_text):
    return (cipher_text ** d) % n

# Simple message to encode
msg = 630

# encrypt then decrypt
enc_msg = encrypt(msg)
dec_msg = decrypt(enc_msg)

print("Original Message:",msg)
print("Encrypted Message:",enc_msg)
print("Decrypted Message:",dec_msg)