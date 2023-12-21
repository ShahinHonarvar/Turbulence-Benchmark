
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(nums):
    x = nums[645]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            num_str = str(num)
            if '0' not in num_str:
                flag = True
                for i in range(len(num_str)):
                    if not is_prime(int(num_str[i:])):
                        flag = False
                        break
                if flag:
                    primes.append(num)
    return sorted(primes)
