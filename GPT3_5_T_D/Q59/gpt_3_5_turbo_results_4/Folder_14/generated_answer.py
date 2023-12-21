
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def remove_leading_digit(n):
    return int(str(n)[1:])

def all_left_truncatable_prime(numbers):
    x = numbers[78]
    left_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            temp_num = num
            while temp_num > 0:
                if not is_prime(temp_num):
                    break
                temp_num = remove_leading_digit(temp_num)
            else:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)
