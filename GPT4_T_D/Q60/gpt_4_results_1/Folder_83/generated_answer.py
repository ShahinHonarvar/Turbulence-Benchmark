
import sympy

def all_left_right_truncatable_prime(nums):
    x = nums[24]
    primes = []
    for num in range(23, x + 1):  # Prime numbers start at 23 for left-and-right-truncatable
        if sympy.isprime(num):
            str_num = str(num)
            if '0' in str_num:
                continue
            truncatable = True
            for i in range(1, len(str_num)):
                if not (sympy.isprime(int(str_num[i:])) and sympy.isprime(int(str_num[:-i]))):
                    truncatable = False
                    break
            if truncatable:
                primes.append(num)
    return sorted(primes)
