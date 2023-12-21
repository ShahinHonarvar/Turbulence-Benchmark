
from sympy import isprime

def is_left_truncatable_prime(n):
    s = str(n)
    if '0' in s:
        return False
    while len(s) > 0:
        if not isprime(int(s)):
            return False
        s = s[1:]
    return True

def all_left_truncatable_prime(arr):
    x = arr[93]
    result = [i for i in range(x) if is_left_truncatable_prime(i)]
    result.sort()
    return result
