
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

def left_truncatable_primes_less_than(x):
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' not in str(num):
            temp = str(num)
            while temp:
                if not is_prime(int(temp)):
                    break
                temp = temp[1:]
            else:
                left_truncatable_primes.append(num)
    return left_truncatable_primes

def all_left_truncatable_prime(numbers):
    x = numbers[61]
    return sorted(left_truncatable_primes_less_than(x))
