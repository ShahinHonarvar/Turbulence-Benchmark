
import math

def all_left_truncatable_prime(numbers):
    x = numbers[23]
    primes = []
    for num in range(10, x):
        if is_prime(num) and check_truncatable(num):
            primes.append(num)
    return primes

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def check_truncatable(num):
    str_num = str(num)
    for i in range(len(str_num)):
        trunc = int(str_num[i:])
        if not is_prime(trunc):
            return False
    return True
