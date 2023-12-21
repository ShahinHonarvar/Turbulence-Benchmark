
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[70]
    result = []
    for i in range(2, x):
        if '0' in str(i):
            continue
        else:
            str_i = str(i)
            flag = 0
            for j in range(len(str_i)):
                if isprime(int(str_i[j:])):
                    continue
                else:
                    flag = 1
                    break
            if flag == 0:
                result.append(i)
    return sorted(result)
