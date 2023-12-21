
import math
   
def is_prime(n):
    if n == 2:
       return True
    if n < 2 or n % 2 == 0:
       return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True

def all_left_truncatable_prime(numbers):
    x = numbers[41]
    result = []
    for num in range(x - 1, 10, -1):
        if '0' in str(num):
            continue
        truncatable = True
        for i in range(len(str(num))):
            truncated_num = int(str(num)[i:])
            if not is_prime(truncated_num):
                truncatable = False
                break
        if truncatable:
            result.append(num)
    return result
