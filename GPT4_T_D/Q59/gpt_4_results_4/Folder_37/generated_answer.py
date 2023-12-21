
from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[35]
    
    def left_truncatable(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])):
                return False
        return True

    left_trunc_primes = [i for i in range(2, x) if left_truncatable(i)]
    return sorted(left_trunc_primes, reverse=True)
