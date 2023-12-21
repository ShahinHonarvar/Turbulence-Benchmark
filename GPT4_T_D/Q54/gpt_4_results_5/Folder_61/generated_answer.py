
from sympy import isprime

def all_right_truncatable_prime(tup):
    x = tup[3]
    right_truncatable_primes = []
    
    def check_right_truncatable(num):
        str_num = str(num)
        for i in range(len(str_num)):
            if not isprime(int(str_num[:-i or None])):
                return False
        return True
    
    for i in range(2, x):
        if check_right_truncatable(i):
            right_truncatable_primes.append(i)
    
    return sorted(right_truncatable_primes, reverse=True)
