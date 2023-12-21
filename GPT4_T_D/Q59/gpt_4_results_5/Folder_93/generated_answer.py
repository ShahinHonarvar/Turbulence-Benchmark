
from sympy import isprime

def all_left_truncatable_prime(tuple):
    x = tuple[11]
    left_truncatable_primes = []
    for num in range(2,x):
        if "0" not in str(num) and isprime(num):
            truncatable = True
            for i in range(1,len(str(num))):
                if not isprime(int(str(num)[i:])):
                    truncatable = False
                    break
            if truncatable:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)
