
from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[88]
    primes = []
    for num in range(11, x):
        if '0' not in str(num):
            numbers = [str(num)[i:] for i in range(len(str(num)))]
            if all(isprime(int(num)) for num in numbers):
                primes.append(num)
    return sorted(primes)
