
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[41]
    primes = [str(i) for i in range(10,x) if isprime(i)]
    truncatable_primes = []
    for prime in primes:
        if '0' not in prime:
            check = True
            while len(prime) > 1:
                prime = prime[1:]
                if not isprime(int(prime)):
                    check = False
                    break
            if check:
                truncatable_primes.append(int(prime))
    return sorted(truncatable_primes,reverse=True)
