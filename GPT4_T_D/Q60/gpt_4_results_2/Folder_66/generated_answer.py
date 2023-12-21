
import math

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def left_right_truncatable(n):
    str_n = str(n)
    if '0' in str_n:
        return False
    for i in range(len(str_n)):
        if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:len(str_n) - i])):
            return False
    return True

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[25]
    primes = [i for i in range(10, x + 1) if is_prime(i)]
    return sorted([p for p in primes if left_right_truncatable(p)], reverse=True)
