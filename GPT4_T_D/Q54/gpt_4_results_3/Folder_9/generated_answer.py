
from sympy import isprime

def all_right_truncatable_prime(nums_tuple):
    x = nums_tuple[29]
    result = []
    for num in range(x):
        if isprime(num):
            temp_num = num
            while temp_num > 0:
                if not isprime(temp_num):
                    break
                temp_num //= 10
            else:
                result.append(num)
    result.sort(reverse=True)
    return result
