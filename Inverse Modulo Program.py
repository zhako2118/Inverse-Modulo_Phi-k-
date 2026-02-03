# Zhalgas Tileumuratin for MATH-396. Just for fun:)
# this program finds the inverse modulo for a number in the format of ax =~ 1 (mod m)
# given that a and m are integers not equal to 0
# Zhalgas Tileumuratin for MATH-396. Just for fun :)
# This program finds the inverse modulo for a number in the format ax ≡ 1 (mod m)
# given that a and m are non-zero integers
import math
#general euclidean fuction formula
def extended_gcd_alg(a, b):
    if b == 0:
        return a, 1, 0
    else:
        g, x1, y1 = extended_gcd_alg(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return g, x, y

print("This program finds the inverse modulo a⁻¹ (mod m), given non-zero integers a and m")

a = int(input("Give a value for a: "))
m = int(input("Give a value for m: "))

print(f"\nNow we find an inverse modulo for {a} (mod {m})")

# Step 1: Check gcd(a, m)
g = math.gcd(a, m)
print(f"The gcd is {g}")

if g != 1:
    print("Inverse modulo does NOT exist!")
else:
    print("Inverse exists, proceeding...\n")

    # Step 2: Extended Euclidean Algorithm
    g, x, y = extended_gcd_alg(a, m)

    print(f"Solution to {a}x + {m}y = 1:")
    print(f"x = {x}, y = {y}")

    # Step 3: x is the inverse modulo (reduce mod m)
    inverse = x 
    print(f"Hence, the inverse modulo is a⁻¹ ≡ {inverse} (mod {m})")


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


# Euler's Theorem
# if gcd (a,m) = 1, then a ^φ(m) ≡ 1 mod m