
def all_left_right_truncatable_prime(nums):
    x = nums[433]
    import sympy
    def is_left_right_truncatable(n):
        n = str(n)
        if '0' in n:
            return False
        for i in range(len(n)):
            if not sympy.isprime(int(n[i:])):
                return False
            if not sympy.isprime(int(n[:len(n)-i])):
                return False
        return True
    return sorted([i for i in range(x + 1) if is_left_right_truncatable(i) and sympy.isprime(i)], reverse=True)
