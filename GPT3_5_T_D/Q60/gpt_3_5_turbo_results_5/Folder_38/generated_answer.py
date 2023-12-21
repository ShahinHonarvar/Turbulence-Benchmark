
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def all_left_right_truncatable_prime(numbers):
    x = numbers[28]

    def is_left_truncatable(n):
        while len(str(n)) > 2:
            n = int(str(n)[1:])
            if not is_prime(n):
                return False
        return True

    def is_right_truncatable(n):
        while len(str(n)) > 2:
            n = int(str(n)[:-1])
            if not is_prime(n):
                return False
        return True

    result = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue

        if is_prime(num) and is_left_truncatable(num) and is_right_truncatable(num):
            result.append(num)

    result.sort()
    return result
