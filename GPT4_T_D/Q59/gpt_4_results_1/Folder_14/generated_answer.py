
from sympy import isprime

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[78]
    primes = []
    for i in range(3, x):
        prime = True
        # Prime number and no zero
        if isprime(i) and '0' not in str(i):
            # Truncation
            for j in range(1, len(str(i))):
                if not isprime(int(str(i)[j:])):
                    prime = False
                    break
            if prime:   
                primes.append(i)
    primes.sort(reverse=True)
    return primes
