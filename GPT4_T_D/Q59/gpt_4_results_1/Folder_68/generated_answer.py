
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[1]
    prime_list = list(filter(isprime, range(2, x)))
    result = []
    for prime in prime_list:
        flag = True
        if '0' not in str(prime):
            temp = str(prime)
            while len(temp) > 1:
                temp = temp[1:]
                if not isprime(int(temp)):
                    flag = False
                    break
        else:
            flag = False
        if flag:
            result.append(prime)
    result.sort(reverse=True)
    return result
