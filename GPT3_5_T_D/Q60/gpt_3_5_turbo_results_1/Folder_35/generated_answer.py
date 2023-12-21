
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if num < 10:
            continue
        str_num = str(num)
        if '0' in str_num:
            continue
        is_trunc_prime = True
        for i in range(len(str_num)):
            left_trunc = int(str_num[i:])
            right_trunc = int(str_num[:len(str_num) - i])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                is_trunc_prime = False
                break
        if is_trunc_prime:
            primes.append(num)
    primes.sort()
    return primes
