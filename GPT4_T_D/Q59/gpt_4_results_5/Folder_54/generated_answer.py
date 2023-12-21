
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[88]
    results = []
    for number in range(11, x):
        if '0' in str(number):
            continue
        truncatable = True
        for i in range(len(str(number))):
            if not isprime(int(str(number)[i:])):
                truncatable = False
                break
        if truncatable:
            results.append(number)
    return sorted(results, reverse=True)
