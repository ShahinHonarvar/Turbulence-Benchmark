
from sympy import isprime

def all_left_right_truncatable_prime(input_tuple):
    
    def is_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        n_len = len(str_n)
        for i in range(n_len):
            if not isprime(int(str_n[i:])):
                return False
            if not isprime(int(str_n[:n_len-i])):
                return False
        return True

    x = input_tuple[87]
    result = [i for i in range(10, x+1) if is_truncatable(i)]
    return sorted(result)
