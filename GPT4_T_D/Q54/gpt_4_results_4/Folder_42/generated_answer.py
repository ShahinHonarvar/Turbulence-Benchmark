
from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[64]
    result = []
    for num in range(2, x):
        stri_num = str(num)
        if all(isprime(int(stri_num[:i])) for i in range(1, len(stri_num) + 1)):
            result.append(num)
    return sorted(result, reverse=True)
