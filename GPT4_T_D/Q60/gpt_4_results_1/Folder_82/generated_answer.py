
from sympy import isprime

def all_left_right_truncatable_prime(tup):
    def is_truncatable(n):
        str_n = str(n)
        return all(isprime(int(str_n[i:])) and isprime(int(str_n[:len(str_n)-i])) for i in range(len(str_n)))

    x = tup[69]
    return sorted(filter(lambda n: isprime(n) and is_truncatable(n) and ('0' not in str(n)), range(10, x+1)), reverse=True)
