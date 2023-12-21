
import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[24]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            temp = str(i)
            is_right_truncatable = True
            for j in range(len(temp)-1):
                temp = temp[:-1]
                if not is_prime(int(temp)):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)
