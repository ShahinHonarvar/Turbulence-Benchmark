
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    def is_truncatable_prime(n):
        if '0' in str(n):  # check if number contains 0
            return False
        while len(str(n)) > 2:
            n = int(str(n)[1:-1])
            if not isprime(n):
                return False
        return True

    x = nums[429]
    result = [i for i in range(2, x+1) if is_truncatable_prime(i)]
    return sorted(result, reverse=True)
