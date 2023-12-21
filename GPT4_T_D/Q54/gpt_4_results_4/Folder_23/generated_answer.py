
from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[77]
    result = []
    for number in range(x):
        is_truncatable = True
        while number:
            if isprime(number):
                number //= 10
            else:
                is_truncatable = False
                break
        if is_truncatable and number == 0:
            result.append(number)
    return sorted(result, reverse=True)
