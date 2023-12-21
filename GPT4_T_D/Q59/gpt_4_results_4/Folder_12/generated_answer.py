
from sympy import isprime

def all_left_truncatable_prime(tup):
    # check for left truncatable prime
    def check(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(len(s)):
            if not isprime(int(s[i:])):
                return False
        return True

    x = tup[70]
    result = []
    primes = [isprime(n) for n in range(2, x)]

    for i, prime in enumerate(primes):
        if prime and check(i + 2):
            result.append(i+2)
    
    result.sort(reverse=True)
    return result
