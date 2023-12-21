
from sympy import isprime

def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[86]
    
    def is_truncatable(n):        
        str_n = str(n)
        if '0' in str_n:
            return False
        length = len(str_n)
        for i in range(length):
            left = str_n[i:]
            right = str_n[:length - i]
            if not (isprime(int(left)) and isprime(int(right))):
                return False
        return True

    return [i for i in range(10, x + 1) if is_truncatable(i)]
