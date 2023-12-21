
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[96]
    
    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not isprime(int(str(n)[i:])):
                return False
        return True

    lst_primes = [i for i in range(11, x) if is_left_truncatable_prime(i)]
    return sorted(lst_primes, reverse=True)
