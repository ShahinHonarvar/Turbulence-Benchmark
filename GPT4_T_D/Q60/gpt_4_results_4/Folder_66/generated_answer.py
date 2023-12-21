
import math

def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True

def get_left_right_truncations(num):
    str_num = str(num)
    truncations = []
    for i in range(1, len(str_num)):
        truncations.append(int(str_num[i:]))
        truncations.append(int(str_num[:-i]))
    return truncations

def check_no_zero(num):
    if '0' in str(num):
        return False
    return True

def check_left_right_truncable_prime(num):
    if not check_prime(num) or not check_no_zero(num):
        return False
    truncations = get_left_right_truncations(num)
    for trunc in truncations:
        if not check_prime(trunc):
            return False
    return True

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[25]
    truncatable_primes = []
    for num in range(2, x + 1):
        if check_left_right_truncable_prime(num):
            truncatable_primes.append(num)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
