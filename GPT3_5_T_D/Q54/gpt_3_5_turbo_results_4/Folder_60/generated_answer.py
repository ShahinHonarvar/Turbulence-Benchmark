
import math

def is_prime(n):
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

def all_right_truncatable_prime(numbers):
    x = numbers[87]
    results = []
    for num in range(2, x):
        if is_prime(num):
            truncatable = True
            for i in range(len(str(num))):
                if not is_prime(int(str(num)[:-i])):
                    truncatable = False
                    break
            if truncatable:
                results.append(num)
    return sorted(results)
