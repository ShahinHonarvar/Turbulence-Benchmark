
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[36]
    results = []
    for num in range(x - 1, 9, -1):
        if is_prime(num):
            truncatable = True
            str_num = str(num)
            for i in range(1, len(str_num)):
                trunc_num = int(str_num[:-i])
                if not is_prime(trunc_num):
                    truncatable = False
                    break
            if truncatable:
                results.append(num)
    return sorted(results, reverse=True)
