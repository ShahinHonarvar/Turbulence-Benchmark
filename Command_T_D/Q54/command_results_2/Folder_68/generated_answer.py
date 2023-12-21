import sys
import functools
    " version 3.6 or higher is required."
@functools.lru_cache(maxsize=10**5)
def all_right_truncatable_prime(n):
    # Function to generate all primes that are right-truncatable
    def generate_right_truncatable_primes(n):
        # Base case: n cannot be a prime number
        if n < 2:
            return []
        # Base case: if n is already a prime number, then there is
        # nothing to remove so it is automatically right-truncatable
        if all(n % d != 0 for d in range(2, int(n**(0.5)) + 1)):
            yield n
        # Recurse: try removing the last digit and check if the number is
        # still a prime number
        for d in range(2, int(n**(0.5)) + 1):
            if n % d == 0:
                continue
            n //= 10**(d - 1)
            yield from generate_right_truncatable_primes(n)
    # Generate a sorted list of right-truncatable primes and return it
    return sorted(set(generate_right_truncatable_primes(n)), reverse=True)
