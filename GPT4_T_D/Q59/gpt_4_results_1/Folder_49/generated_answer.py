
from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[14]
    primes_under_x = [str(num) for num in range(2, x) if isprime(num)]
    left_truncatable_primes = []
    for prime in primes_under_x:
        if '0' in prime:
            continue
        else:
            is_left_truncatable = True
            for i in range(1, len(prime)):
                if not isprime(int(prime[i:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                left_truncatable_primes.append(int(prime))
    return sorted(left_truncatable_primes)
