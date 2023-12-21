
from sympy import isprime

def all_left_truncatable_prime(input_tuple):
    x = input_tuple[767]

    # Helper function to check if a number is left truncatable prime
    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False

        return all(isprime(int(str(n)[i:])) for i in range(len(str(n))))
    
    left_truncatable_primes = [i for i in range(x) if is_left_truncatable_prime(i)]
    return sorted(left_truncatable_primes, reverse=True)
