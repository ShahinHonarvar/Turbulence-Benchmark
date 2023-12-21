
from sympy import isprime

def all_right_truncatable_prime(tpl):
    x = tpl[41]

    def check_right_truncatable(n):
        str_n = str(n)

        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])):
                return False

        return True

    return sorted([i for i in range(2, x) if check_right_truncatable(i)])
