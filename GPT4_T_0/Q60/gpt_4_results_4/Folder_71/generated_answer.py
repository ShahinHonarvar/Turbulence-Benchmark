
from sympy import isprime

def all_left_right_truncatable_prime(tup):
    x = tup[22]
    truncatable_primes = []
    for num in range(10, x+1):
        if '0' in str(num):
            continue
        str_num = str(num)
        is_truncatable = True
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])) or not isprime(int(str_num[:len(str_num)-i])):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)
