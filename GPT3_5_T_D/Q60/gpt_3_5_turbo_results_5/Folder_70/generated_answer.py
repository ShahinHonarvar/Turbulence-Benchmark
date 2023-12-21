
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if num < 23:
            continue
        if '0' in str(num):
            continue

        is_lrt_prime = True
        for i in range(1, len(str(num))):
            left_trunc = int(str(num)[i:])
            right_trunc = int(str(num)[:i])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                is_lrt_prime = False
                break
        if is_lrt_prime:
            primes.append(num)
    primes.sort(reverse=True)
    return primes
