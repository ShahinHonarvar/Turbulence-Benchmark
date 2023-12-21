
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    if len(nums) < 631:
        return []
    limit = nums[630]
    result = []
    for num in range(11, limit+1):
        str_num = str(num)
        if '0' in str_num:
            continue
        length = len(str_num)
        left_right_truncatable = True
        for i in range(length):
            if not (isprime(int(str_num[i:])) and isprime(int(str_num[:length-i]))):
                left_right_truncatable = False
                break
        if left_right_truncatable:
            result.append(num)
    return sorted(result, reverse=True)
