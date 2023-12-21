
from sympy import isprime

def all_left_truncatable_prime(tuple_of_ints):
    x = tuple_of_ints[54]
    primes = [str(i) for i in range(2, x) if isprime(i) and '0' not in str(i)]
    left_truncatable_primes = []
    for prime in primes:
        primes_created = [prime[i:] for i in range(len(prime))]
        if all(isprime(int(num)) for num in primes_created):
            left_truncatable_primes.append(int(prime))
    return sorted(left_truncatable_primes)
