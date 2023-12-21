
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[945]
    result = []
    for i in range(2, x):
        if is_prime(i):
            num_str = str(i)
            while len(num_str) > 0:
                if not is_prime(int(num_str)):
                    break
                num_str = num_str[:-1]
            else:
                result.append(i)
    return sorted(result, reverse=True)
