
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[74]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            num_str = str(num)
            is_right_truncatable = True
            for i in range(len(num_str)-1):
                trunc_num = int(num_str[:-i-1])
                if not is_prime(trunc_num):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)
