
from sympy import isprime

def all_left_right_truncatable_prime(tuples):
    x = tuples[370]
    all_primes = []

    def check_prime(n):
        n = str(n)
        if '0' in n:
            return False
        for i in range(len(n)):
            if not (isprime(int(n[i:])) and isprime(int(n[:len(n) - i]))):
                return False
        return True
    
    for i in range(11, x+1, 2):
        if check_prime(i):
            all_primes.append(i)

    return sorted(all_primes, reverse=True)
