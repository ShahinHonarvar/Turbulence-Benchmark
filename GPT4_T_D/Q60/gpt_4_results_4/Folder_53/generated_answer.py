
from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[86]
    results = []
    for number in range(10, x + 1):
        if '0' in str(number):
            continue
        is_truncatable = True
        for i in range(len(str(number))):
            left_truncated = int(str(number)[i:])
            right_truncated = int(str(number)[:-i-1]) if i != 0 else number
            if not isprime(left_truncated) or not isprime(right_truncated):
                is_truncatable = False
                break
        if is_truncatable:
            results.append(number)
    return sorted(results, reverse=True)
