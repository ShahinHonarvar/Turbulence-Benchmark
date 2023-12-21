
from sympy import isprime

def all_left_right_truncatable_prime(tup):
    x = tup[767]
    primes = []

    for num in range(2, x+1):
        if '0' in str(num):
            continue
        if isprime(num):
            str_num = str(num)
            truncatable = True
            for i in range(1, len(str_num)):
                if not isprime(int(str_num[i:])) or not isprime(int(str_num[:-i])):
                    truncatable = False
                    break
            if truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)
