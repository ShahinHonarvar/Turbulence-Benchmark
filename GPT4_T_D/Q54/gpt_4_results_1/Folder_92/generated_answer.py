
def all_right_truncatable_prime(nums):
    import sympy

    def is_right_truncatable(n):
        while n != 0:
            if not sympy.isprime(n):
                return False
            n = n // 10
        return True

    x = nums[7]
    rtp_nums = [i for i in range(x) if is_right_truncatable(i)]
    return sorted(rtp_nums)
