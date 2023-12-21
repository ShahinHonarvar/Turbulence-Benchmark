
from sympy import isprime

def all_left_truncatable_prime(tuple_values):
    x = tuple_values[32]
    
    def is_left_truncatable_prime(p):
        if '0' in str(p):
            return False
        return all(isprime(int(str(p)[i:])) for i in range(len(str(p))))

    return sorted(filter(is_left_truncatable_prime, filter(isprime, range(2, x))))
