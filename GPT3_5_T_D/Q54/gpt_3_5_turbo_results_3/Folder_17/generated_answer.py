
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[36]
    result = []
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            temp = str(num)
            while temp != "":
                if not is_prime(int(temp)):
                    break
                temp = temp[:-1]
            else:
                result.append(num)
    return sorted(result, reverse=True)
