
from sympy import isprime

def all_left_truncatable_prime(integers):
    x = integers[18]
    
    def check_left_truncate(num):
        if '0' in str(num):
            return False

        for i in range(len(str(num))):
            if not isprime(int(str(num)[i:])):
                return False
        return True

    left_truncatable_primes = [i for i in range(x) if check_left_truncate(i)]
    return sorted(left_truncatable_primes, reverse=True)
