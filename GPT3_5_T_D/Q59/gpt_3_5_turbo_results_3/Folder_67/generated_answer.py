
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[71]
    result = []
    for num in range(x - 1, 0, -1):
        if '0' not in str(num):
            is_truncatable_prime = True
            str_num = str(num)
            for i in range(len(str_num)):
                if not is_prime(int(str_num[i:])):
                    is_truncatable_prime = False
                    break
            if is_truncatable_prime:
                result.append(num)
    return result
