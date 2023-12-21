
from sympy import isprime

def all_left_right_truncatable_prime(tup):
    x = tup[98]
    primes = []
    for num in range(11, x + 1):
        if '0' in str(num):
            continue
        left_right_truncatable = True
        for i in range(len(str(num))):
            if not isprime(int(str(num)[i:])) or not isprime(int(str(num)[:len(str(num))-i])):
                left_right_truncatable = False
                break
        if left_right_truncatable:
            primes.append(num)
    return sorted(primes)
