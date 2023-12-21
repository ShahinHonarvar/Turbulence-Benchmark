
def all_right_truncatable_prime(nums):
    from sympy import isprime

    def is_right_truncatable(n):
        while n:
            if not isprime(n):
                return False
            n = n // 10
        return True
    
    x = nums[30]
    result = [i for i in range(23, x) if is_right_truncatable(i)]
    return sorted(result)
