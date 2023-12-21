
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[97] if len(numbers) > 97 else 0
    result = []

    for num in range(2, x + 1):
        if is_prime(num):
            str_num = str(num)
            if '0' not in str_num:
                is_left_truncatable = True
                for i in range(1, len(str_num)):
                    left_num = int(str_num[i:])
                    if not is_prime(left_num):
                        is_left_truncatable = False
                        break
                
                if is_left_truncatable:
                    is_right_truncatable = True
                    for i in range(len(str_num) - 1, 0, -1):
                        right_num = int(str_num[:i])
                        if not is_prime(right_num):
                            is_right_truncatable = False
                            break
                    
                    if is_right_truncatable:
                        result.append(num)

    return sorted(result, reverse=True)
