# Zhalgas Tileumuratin for MATH-396. Just for fun:)
# this program finds the inverse modulo for a number in the format of ax =~ 1 (mod m)
# given that a and m are integers not equal to 0
import math

# Find the inverse of a (mod m)
print ('This program finds an inverse modulo (a^-1) for any expression in the format of a (mod m), given that a and m are non-zero integers')
a = int(input ('Give a value for a: '))
m = int(input ('Give a value for m: '))

print (f'Now we find an inverse modulo for {a} (mod {m})')
# Step 1: check if gcd (a,m) = 1
g = math.gcd(a, m)

print (f'The gcd is {g}')
# if not approved, print "No inverse modulo"
if g != 1:
     print ('Inverse modulo does NOT exist!')
# otherwise approved, move to Step 2
else:
     print ('Inverse exists, proceeding...')
     
# Step 2: Find x,y such that ax + my = 1; given that x and y are integers
# Extended Euclidean Algorithm
def extended_gcd_alg(a, b):
     if b == 0:
          return a, 1, 0 
     else:
        g, x1, y1 = extended_gcd_alg(b, a % b)
        x = y1
        y = x1 - (a//b) * y1
        return g, x, y

g, x, y = extended_gcd_alg (a,m)
print (f'Solution to {a}x + {m}y = 1: ')
print (f'x = {x}, y = {y}')

# Step 3: x is the a^-1 of a (or inverse modulo)
print (f'Hence, the inverse modulo a^-1 = {x}')


# Ask for the phi of k, where k is any positive integer
print('Do you want me to compute φ(k)? Please answer yes/no')
y_n = input('yes/no: ').strip().lower()

# General Prime Factorization
def prime_factorization(n):
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = 1
    return factors


# General Euler Function
def phi(n):
    factors = prime_factorization(n)
    result = 1

    print(f"Prime factorization: {factors}")

    for p, e in factors.items():
        term = p**e - p**(e-1)
        print(f"φ({p}^{e}) = {p**e} - {p**(e-1)} = {term}")
        result *= term

    return result


# Do you want to run this program
if y_n == "yes":
    k = int(input("Enter k: "))
    phiofk = phi(k)
    print(f"φ({k}) = {phiofk}")
else:
    print("Program ended.")
