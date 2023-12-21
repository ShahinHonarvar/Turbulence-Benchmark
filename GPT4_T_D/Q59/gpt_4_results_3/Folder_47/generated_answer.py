
from sympy import isprime

def all_left_truncatable_prime(num_tuple):
    # get the 49th element
    x = num_tuple[49]

    def is_left_truncatable_prime(p):
        # a prime should not contain 0
        if '0' in str(p):
            return False
            
        # if the leading leftmost digit is successively removed, check if all resulting numbers are prime
        return all(isprime(int(str(p)[i:])) for i in range(len(str(p))))

    return sorted(p for p in range(11, x) if isprime(p) and is_left_truncatable_prime(p))
