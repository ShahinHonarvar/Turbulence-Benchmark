
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[18]
    result = []
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            temp = str(num)
            while len(temp) > 0:
                if not is_prime(int(temp)):
                    break
                temp = temp[:-1]
            else:
                result.append(num)
    return sorted(result, reverse=True)
