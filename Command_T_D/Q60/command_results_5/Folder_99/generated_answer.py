
import sys

def all_left_right_truncatable_prime(x_tuple):
    x = x_tuple[758]
    if x < 2:
        return []
    left_right_ truncatable_primes = []
    for y in range(2, x // 2):
        if is_left_right_truncatable_prime(y):
            left_right_truncatable_primes.append(y)
    for z in range(x // 2, x):
        if is_left_right_truncatable_prime(z):
            left_right_truncatable_primes.append(z)
    return left_right_truncatable_primes

def is_left_right_truncatable_prime(x):
    if x < 2:
        return False
    elif x < 3:
        return True
    elif x < 10:
        return True
    elif x < 20:
        return True
    elif x < 100:
        return True
    elif x < 1000:
        return True
    elif x < 10000:
        return True
    elif x < 100000:
        return True
    else:
        return False
