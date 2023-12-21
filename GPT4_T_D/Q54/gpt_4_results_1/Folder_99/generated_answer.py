
from sympy import isprime

def all_right_truncatable_prime(tuple_of_positive_integers):
    def is_right_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])):
                return False
        return True

    x = tuple_of_positive_integers[758]

    return sorted([i for i in range(2, x) if is_right_truncatable_prime(i)])
