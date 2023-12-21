
from sympy import isprime

def all_left_right_truncatable_prime(tpl):
    def is_truncatable(n):
        n_str = str(n)
        n_len = len(n_str)
        if "0" in n_str:
            return False
        for i in range(n_len):
            n_right = int(n_str[i:])
            n_left = int(n_str[:n_len-i])
            if not isprime(n_right) or not isprime(n_left):
                return False
        return True

    x = tpl[784]
    return [i for i in range(2, x+1) if is_truncatable(i)]
