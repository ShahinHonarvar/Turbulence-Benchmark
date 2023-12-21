
from sympy import isprime

def all_left_right_truncatable_prime(tup):
    def is_left_right_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])) or not isprime(int(str_n[:len(str_n)-i])):
                return False
        return True

    x = tup[370]
    return sorted([i for i in range(10, x+1) if is_left_right_truncatable_prime(i)], reverse=True)
