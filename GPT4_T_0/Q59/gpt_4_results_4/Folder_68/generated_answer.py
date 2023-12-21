
from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[1]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        else:
            str_num = str(num)
            primes = [isprime(int(str_num[i:])) for i in range(len(str_num))]
            if all(primes):
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)
