
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[79]
    result = []
    for num in range(x-1, 1, -1):
        if is_prime(num):
            is_right_truncatable = True
            temp = num // 10
            while temp > 0:
                if not is_prime(temp):
                    is_right_truncatable = False
                    break
                temp //= 10
            if is_right_truncatable:
                result.append(num)
    result.sort(reverse=True)
    return result
