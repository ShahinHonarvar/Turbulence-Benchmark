
from sympy import primerange

def all_left_right_truncatable_prime(nums):
    x = nums[69]
    factors = list(primerange(1, x+1))

    truncatable = []
    for num in factors:
        if '0' not in str(num):
            length = len(str(num))
            left_truncatable = all(int(str(num)[i:]) in factors for i in range(length))
            right_truncatable = all(int(str(num)[:i]) in factors for i in range(1, length))

            if left_truncatable and right_truncatable:
                truncatable.append(num)

    return sorted(truncatable, reverse=True)
