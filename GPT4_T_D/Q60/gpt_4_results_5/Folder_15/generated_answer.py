
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[6]
    prime_nums = []

    for num in range(2, x+1):
        str_num = str(num)
        if '0' in str_num:
            continue
        prime = True
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])) or not isprime(int(str_num[:len(str_num)-i])):
                prime = False
                break
        if prime:
            prime_nums.append(num)
    
    return sorted(prime_nums, reverse=True)
