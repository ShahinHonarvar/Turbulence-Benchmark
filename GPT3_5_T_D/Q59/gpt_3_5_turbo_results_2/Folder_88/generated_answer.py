
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[93]
    result = []
    for i in range(10, x):
        if all(is_prime(int(str(i)[j:])) for j in range(len(str(i)))):
            result.append(i)
    return sorted(result)
