
from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[78]
    left_truncatable_primes = []
    for num in range(2, x):
        if num % 10 == 0:
            continue
        str_num = str(num)
        is_valid = True
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])):
                is_valid = False
                break
        if is_valid:
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)
