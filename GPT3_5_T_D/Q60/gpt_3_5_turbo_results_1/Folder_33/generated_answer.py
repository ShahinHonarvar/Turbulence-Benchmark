
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
    for x in numbers:
        if x < 10:
            continue
        str_x = str(x)
        if '0' in str_x:
            continue
        is_truncatable = True
        for i in range(len(str_x) - 1):
            if not is_prime(int(str_x[:i+1])) or not is_prime(int(str_x[i+1:])):
                is_truncatable = False
                break
        if is_truncatable:
            primes.append(x)
    return sorted(primes, reverse=True)
