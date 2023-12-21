
from sympy import isprime

def all_left_truncatable_prime(tuple):
    x = tuple[74]
    primes = []

    def left_truncatable(p):
        p_str = str(p)
        for i in range(len(p_str)):
            if not isprime(int(p_str[i:])):
                return False
        return True

    for i in range(11, x):
        if i % 10 and all(map(isprime, (int(str(i)[j:]) for j in range(len(str(i)))))):
            primes.append(i)

    primes.sort()
    return primes
