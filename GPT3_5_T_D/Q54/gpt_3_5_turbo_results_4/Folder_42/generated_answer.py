
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[64]
    result = []
    for i in range(x-1, 1, -1):
        if is_prime(i):
            truncatable = True
            digits = str(i)
            for j in range(len(digits)-1):
                if not is_prime(int(digits[:j+1])):
                    truncatable = False
                    break
            if truncatable:
                result.append(i)
    return sorted(result, reverse=True)
