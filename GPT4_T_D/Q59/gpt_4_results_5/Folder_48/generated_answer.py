
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[835]
    primes = []

    for i in range(11,x):
        str_num = str(i)
        if '0' not in str_num:
            check = [isprime(int(str_num[j:])) for j in range(len(str_num))]
            if all(check):
                primes.append(i)
    return sorted(primes)
