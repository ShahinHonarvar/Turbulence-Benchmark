
import math

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[35]
    result = []
    for num in range(x-1, 1, -1):
        if is_prime(num):
            num_str = str(num)
            is_truncatable = True
            for i in range(len(num_str)-1, 0, -1):
                trunc_num = int(num_str[:i])
                if not is_prime(trunc_num):
                    is_truncatable = False
                    break
            if is_truncatable:
                result.append(num)
    return sorted(result, reverse=True)
