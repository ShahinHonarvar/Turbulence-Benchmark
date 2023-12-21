
from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[69]
    result = []
    for num in range(2, x):
        if isprime(num):
            temp = str(num)
            is_right_truncatable_prime = True
            while len(temp) > 1:
                temp = temp[:-1]
                if not isprime(int(temp)):
                    is_right_truncatable_prime = False
                    break
            if is_right_truncatable_prime:
                result.append(num)
    return sorted(result, reverse=True)
