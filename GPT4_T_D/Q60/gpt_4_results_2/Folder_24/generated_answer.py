
import math

def is_prime(n):
    if n < 2:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def is_right_left_truncatable(n):
    for i in range(len(str(n))):
        if not is_prime(int(str(n)[i:])) or not is_prime(int(str(n)[:len(str(n))-i])):
            return False
    return True

def all_left_right_truncatable_prime(tuple):
    x = tuple[65]
    result = []
    for i in range(10, x+1):
        if '0' not in str(i) and is_right_left_truncatable(i):
            result.append(i)
    return sorted(result, reverse=True)
