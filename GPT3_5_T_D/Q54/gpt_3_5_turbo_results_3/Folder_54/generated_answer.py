
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[88]
    right_truncatable_primes = []
    for num in range(x-1, 1, -1):
        if is_prime(num):
            truncatable = True
            str_num = str(num)
            for i in range(1, len(str_num)):
                truncated_num = int(str_num[:-i])
                if not is_prime(truncated_num):
                    truncatable = False
                    break
            if truncatable:
                right_truncatable_primes.append(num)

    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes
