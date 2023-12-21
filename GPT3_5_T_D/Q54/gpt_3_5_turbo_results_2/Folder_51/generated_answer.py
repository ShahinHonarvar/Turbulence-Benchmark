
import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.sqrt(n))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[54]
    results = []
    for num in range(2, x):
        prime = True
        curr_num = num
        while prime and curr_num > 0:
            if not is_prime(curr_num):
                prime = False
            curr_num //= 10 # remove the last digit
        if prime:
            results.append(num)
    return sorted(results)
