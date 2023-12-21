
from sympy import isprime

def all_left_truncatable_prime(tuple_of_nums):
    x = tuple_of_nums[65]
    result = []
    for num in range(2, x):
        str_num = str(num)
        if '0' in str_num:
            continue
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])):
                break
        else:
            result.append(int(str_num))
    result.sort(reverse = True)
    return result
