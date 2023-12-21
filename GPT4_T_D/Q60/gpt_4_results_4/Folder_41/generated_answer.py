
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[46]
    primes = []
    for num in range(2, x + 1):
        num_str = str(num)
        if '0' in num_str or not isprime(int(num_str)):
            continue
        length = len(num_str)
        for i in range(1, length):
            left_str = num_str[i:]
            right_str = num_str[:length-i]
            if not isprime(int(left_str)) or not isprime(int(right_str)):
                break
        else:
            primes.append(num)
    return sorted(primes, reverse=True)
