
from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[36]
    construct_right_truncatable_prime = lambda num: isprime(num) and (len(str(num)) == 1 or construct_right_truncatable_prime(int(str(num)[:-1])))
    return sorted([i for i in range(2, x) if construct_right_truncatable_prime(i)], reverse=True)
