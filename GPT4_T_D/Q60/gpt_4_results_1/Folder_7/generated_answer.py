
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[803]
    truncatable_primes = []
    for num in range(11, x+1):
        if '0' not in str(num):
            str_num = str(num)
            num_length = len(str_num)
            is_truncable = True
            for trunc_len in range(1, num_length):
                left_trunc = int(str_num[trunc_len:])
                right_trunc = int(str_num[:-trunc_len])
                if not isprime(left_trunc) or not isprime(right_trunc):
                    is_truncable = False
            if is_truncable and isprime(num):
                truncatable_primes.append(num)
    return sorted(truncatable_primes)
