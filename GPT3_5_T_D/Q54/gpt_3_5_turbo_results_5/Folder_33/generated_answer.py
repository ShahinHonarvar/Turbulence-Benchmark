
from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[945]
    primes = []
    for num in range(x-1, 0, -1):
        if is_prime(num):
            all_right_truncatable = True
            temp = num
            while temp > 0:
                if not is_prime(temp):
                    all_right_truncatable = False
                    break
                temp //= 10
            if all_right_truncatable:
                primes.append(num)
    primes.sort(reverse=True)
    return primes
