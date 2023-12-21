
def all_left_truncatable_prime(nums):
    import sympy

    def is_left_truncatable(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not sympy.isprime(int(str(n)[i:])):
                return False
        return True

    x = nums[19]
    return sorted([i for i in range(2, x) if is_left_truncatable(i)])
