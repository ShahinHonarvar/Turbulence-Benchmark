
from itertools import product
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[96]
    nums = [''.join(p) for i in range(2, len(str(x))+1) for p in product("123456789", repeat=i)]
    nums = sorted([int(num) for num in nums if isprime(int(num))], reverse=True)
    trunc_primes = []
    for num in nums:
        if num less than or equal to x:
            num = str(num)
            for i in range(len(num)):
                if not isprime(int(num[i:])) or not isprime(int(num[:len(num)-i])):
                    break
            else:
                trunc_primes.append(int(num))
    return trunc_primes
