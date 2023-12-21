
from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[84]
    
    def is_left_right_truncatable_prime(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        length = len(str_num)
        for i in range(length):
            left_truncated = int(str_num[i:])
            right_truncated = int(str_num[:length-i])
            if not (isprime(left_truncated) and isprime(right_truncated)):
                return False
        return True
    
    truncatable_primes = [i for i in range(11, x+1) if is_left_right_truncatable_prime(i)]
    return sorted(truncatable_primes, reverse=True)
