
from sympy import isprime

def all_left_right_truncatable_prime(positive_integers):
    def is_left_right_truncatable_prime(n):
        n = str(n)

        if '0' in n:
            return False

        for i in range(1, len(n)):
            if not (isprime(int(n[i:])) and isprime(int(n[:-i]))):
                return False
        return True

    x = positive_integers[29]
    return sorted([i for i in range(11, x+1) if isprime(i) and is_left_right_truncatable_prime(i)], reverse=True)
