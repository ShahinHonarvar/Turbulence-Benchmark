
import math

def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        temp = str(n)
        while len(temp) > 2:
            if not is_prime(int(temp)):
                return False
            temp = temp[1:-1]
        return is_prime(int(temp))

    x = nums[97]
    result = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)
