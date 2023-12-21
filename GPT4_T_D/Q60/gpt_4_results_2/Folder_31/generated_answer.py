
from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[50]
    primes = []
    
    def is_left_right_truncatable_prime(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        digit_len = len(str_num)
        for i in range(digit_len):
            if not (isprime(int(str_num[i:])) and isprime(int(str_num[:digit_len - i]))):
                return False
        return True

    for num in range(10, x + 1):
        if isprime(num) and is_left_right_truncatable_prime(num):
            primes.append(num)

    primes.sort(reverse=True)

    return primes
