
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[6]
    primes = []
    for num in range(11, x):
        str_num = str(num)
        if '0' not in str_num:
            counter = 0
            for y in range(len(str_num)):
                if isprime(int(str_num[y:])):
                    counter += 1
            if counter == len(str_num):
                primes.append(num)
    primes.sort(reverse=True)
    return primes
