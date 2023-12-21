
from sympy import isprime

def all_left_right_truncatable_prime(tup):
    x = tup[630]
    result = []
    
    def is_left_right_truncatable(n):
        n_str = str(n)
        if '0' in n_str or not isprime(n):
            return False
        for i in range(len(n_str)):
            if not isprime(int(n_str[i:])) or not isprime(int(n_str[:len(n_str) - i])):
                return False
        return True
    
    for i in range(x, 11, -1):  # start at n, go down to 11 (smallest left-and-right truncatable prime)
        if is_left_right_truncatable(i):
            result.append(i)
    return result
