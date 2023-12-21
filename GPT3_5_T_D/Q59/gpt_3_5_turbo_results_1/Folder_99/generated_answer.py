
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[758]
    primes = []
    for i in range(2, x):
        is_trunc_primes = True
        num_str = str(i)
        if '0' not in num_str:
            for j in range(len(num_str)):
                truc_num = int(num_str[j:])
                if not is_prime(truc_num):
                    is_trunc_primes = False
                    break
            if is_trunc_primes:
                primes.append(i)
    return primes
