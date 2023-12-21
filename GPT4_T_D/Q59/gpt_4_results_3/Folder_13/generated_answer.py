
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[784]
    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not isprime(int(str(n)[i:])):
                return False
        return True
    
    return sorted([n for n in range(x) if is_left_truncatable_prime(n)])
