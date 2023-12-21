
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[42]
    numbers = []
    for i in range(10, x):
        if '0' not in str(i) and isprime(i):
            s = str(i)
            while len(s) > 0 and isprime(int(s)):
                s = s[1:]
            if len(s) == 0:
                numbers.append(i)
    return sorted(numbers)
