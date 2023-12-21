
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[37]
    result = []
    for num in range(11, x):
        num_str = str(num)
        if '0' in num_str:
            continue
        is_truncatable_prime = isprime(num) 
        while len(num_str) > 1 and is_truncatable_prime:
            num_str = num_str[1:]
            is_truncatable_prime = isprime(int(num_str))
        if is_truncatable_prime:
            result.append(num)
    result.sort(reverse=True)
    return result
