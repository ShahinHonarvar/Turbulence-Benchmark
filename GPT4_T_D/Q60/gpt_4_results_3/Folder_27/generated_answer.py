
from sympy import isprime

def all_left_right_truncatable_prime(tup):
    def is_left_right_truncatable(number):
        str_num = str(number)
        if '0' in str_num:
            return False
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])) or not isprime(int(str_num[:len(str_num)-i])):
                return False
        return True
        
    x = tup[79]
    truncatable_primes = [i for i in range(11, x+1) if is_left_right_truncatable(i)]
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
