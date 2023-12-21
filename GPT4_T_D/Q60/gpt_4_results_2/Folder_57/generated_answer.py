
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[54]
    primes = []
    for num in range(2, x+1):
        if isprime(num) and '0' not in str(num):
            str_num = str(num)
            flag = True
            for i in range(len(str_num)):
                if not isprime(int(str_num[i:])) or not isprime(int(str_num[:len(str_num)-i])):
                    flag = False
                    break
            if flag:
                primes.append(num)
    return sorted(primes, reverse=True)
