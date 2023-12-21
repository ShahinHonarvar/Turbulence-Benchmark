
import math
def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = math.isqrt(n)
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    if '0' in str(n):
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n = int(str(n)[1:]) if len(str(n)) > 1 else 0
    return True

def all_left_truncatable_prime(t):
    x = t[38]
    ltp_list = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            ltp_list.append(i)
    return sorted(ltp_list, reverse=True)
