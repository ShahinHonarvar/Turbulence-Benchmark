
from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[73]
    result = []

    for i in range(2, x):
        str_i = str(i)
        is_truncatable_prime = True
        while len(str_i) > 0:
            if not isprime(int(str_i)):
                is_truncatable_prime = False
                break
            str_i = str_i[:-1]
        
        if is_truncatable_prime:
            result.append(i)
    return sorted(result, reverse=True)
