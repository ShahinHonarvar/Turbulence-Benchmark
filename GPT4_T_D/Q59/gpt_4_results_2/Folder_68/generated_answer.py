
from sympy import isprime

def all_left_truncatable_prime(tup):
    def is_left_truncatable(num): 
        for i in range(len(str(num))):
            if not isprime(int(str(num)[i:])):
                return False
        return True

    x = tup[1]        
    left_truncatable_primes = []

    for num in range(2, x):
        if '0' not in str(num) and is_left_truncatable(num):
            left_truncatable_primes.append(num)

    left_truncatable_primes.sort(reverse=True)

    return left_truncatable_primes
