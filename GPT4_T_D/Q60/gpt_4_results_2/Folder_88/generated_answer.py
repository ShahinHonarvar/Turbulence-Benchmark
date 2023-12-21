
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[93]
    truncatable_primes = []
    for num in range(10, x+1):
        str_num = str(num)
        if '0' in str_num:
            continue
        len_num = len(str_num)
        for i in range(len_num):
            if not isprime(int(str_num[i:])) or not isprime(int(str_num[:len_num-i])):
                break
        else:
            truncatable_primes.append(num)
    return sorted(truncatable_primes)
