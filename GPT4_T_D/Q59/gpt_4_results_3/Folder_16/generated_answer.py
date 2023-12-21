
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[792]
    result = []
    for num in range(10, x):
        if '0' not in str(num) and isprime(num):
            s = str(num)
            while len(s) > 1:
                s = s[1:]
                if not isprime(int(s)):
                    break
            else:
                result.append(num)
    return sorted(result)
