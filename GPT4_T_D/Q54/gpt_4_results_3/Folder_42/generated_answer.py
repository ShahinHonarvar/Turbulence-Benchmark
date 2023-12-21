
from sympy import isprime

def all_right_truncatable_prime(tup):
    x = tup[64]
    primes = []
    
    for num in range(2, x):
        str_num = str(num)
        while len(str_num) > 0:
            if isprime(int(str_num)):
                str_num = str_num[:-1]
            else:
                break
        else:
            primes.append(num)
    
    return sorted(primes, reverse=True)
