
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[18]
    result = []
    for i in range(x-1, 1, -1):
        if is_prime(i):
            num = str(i)
            is_right_truncatable = True
            for j in range(len(num)-1, 0, -1):
                num = num[:j]
                if not is_prime(int(num)):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                result.append(i)
    result.sort(reverse=True)
    return result
