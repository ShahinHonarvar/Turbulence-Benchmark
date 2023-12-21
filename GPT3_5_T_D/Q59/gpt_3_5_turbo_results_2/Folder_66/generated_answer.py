
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

def all_left_truncatable_prime(numbers):
    x = numbers[25]
    result = []

    for i in range(2, x):
        if '0' in str(i):
            continue
        is_truncatable_prime = True
        number = str(i)
        while len(number) > 1:
            number = number[1:]
            if not is_prime(int(number)):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            result.append(i)

    return sorted(result, reverse=True)
