
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[86]
    result = []
    for num in range(2, x+1):
        if '0' not in str(num):
            truncated_num = num
            is_truncatable_prime = True
            while truncated_num > 0:
                if not is_prime(truncated_num):
                    is_truncatable_prime = False
                    break
                truncated_num = int(str(truncated_num)[1:-1])
            if is_truncatable_prime:
                result.append(num)
    result.sort(reverse=True)
    return result
