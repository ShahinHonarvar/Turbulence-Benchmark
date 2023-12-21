
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[52]
    result = []
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            temp = str(num)
            is_truncatable = True
            for i in range(len(temp)):
                if not is_prime(int(temp[:i+1])):
                    is_truncatable = False
                    break
            if is_truncatable:
                result.append(num)
    return sorted(result, reverse=True)
