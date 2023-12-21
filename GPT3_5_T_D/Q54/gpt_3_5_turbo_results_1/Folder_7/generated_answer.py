
import math

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[803]
    truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            is_truncatable_prime = True
            temp_num = num
            while temp_num > 0:
                if not is_prime(temp_num):
                    is_truncatable_prime = False
                    break
                temp_num = temp_num // 10
            if is_truncatable_prime:
                truncatable_primes.append(num)
    return sorted(truncatable_primes)
