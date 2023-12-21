
from sympy import isprime

def create_left_truncatable_prime(prime):
    str_prime = str(prime)
    for i in range(len(str_prime)):
        if not isprime(int(str_prime[i:])):
            return False
    return True

def all_left_truncatable_prime(input_tuple):
    x = input_tuple[73]
    res=[]
    for i in range(2, x):
        if '0' not in str(i) and isprime(i):
            if create_left_truncatable_prime(i):
                res.append(i)
    return sorted(res, reverse=True)
