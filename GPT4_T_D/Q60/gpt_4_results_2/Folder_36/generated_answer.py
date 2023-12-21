
from sympy import isprime

def all_left_right_truncatable_prime(tup):

    def is_left_right_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False

        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])) or not isprime(int(str_n[:len(str_n)-i])):
                return False
        return True

    limit = tup[992]
    result = [prime for prime in range(10, limit+1) if is_left_right_truncatable(prime)]

    return sorted(result)
