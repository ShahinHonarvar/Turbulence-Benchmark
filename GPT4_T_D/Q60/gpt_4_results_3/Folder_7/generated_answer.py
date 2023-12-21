
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[803]
    result = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' not in str_num and isprime(num):
            temp1 = temp2 = str(num)
            while temp1 and temp2 and isprime(int(temp1)) and isprime(int(temp2)):
                temp1 = temp1[1:]
                temp2 = temp2[:-1]
            if not temp1 and not temp2:
                result.append(num)
    return sorted(result)
