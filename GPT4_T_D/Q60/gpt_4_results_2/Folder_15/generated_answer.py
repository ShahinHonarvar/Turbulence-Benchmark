
from sympy import isprime

def all_left_right_truncatable_prime(t):
    def is_left_right_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])) or not isprime(int(str_n[:len(str_n) - i])):
                return False
        return True

    x = t[6]
    return sorted([n for n in range(11, x + 1) if is_left_right_truncatable(n)], reverse=True)
