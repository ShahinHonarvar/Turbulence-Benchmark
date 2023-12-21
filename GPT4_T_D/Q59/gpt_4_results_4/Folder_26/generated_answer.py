
from itertools import combinations
from sympy import isprime

def all_left_truncatable_prime(tup):

    prime_lst = []
    x = tup[81]
    
    def is_left_truncatable(num):
        if '0' in str(num):
            return False
        for i in range(len(str(num))):
            if not isprime(int(str(num)[i:])):
                return False
        return True
    
    for i in range(2, x):
        if is_left_truncatable(i):
            prime_lst.append(i)

    return sorted(prime_lst, reverse=True)
