
def all_right_truncatable_prime(nums):
    import sympy as sp

    def is_right_truncatable_prime(n):
        while n > 0:
            if not sp.isprime(n):
                return False
            n //= 10
        return True

    x = nums[14]
    rtp_nums = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            rtp_nums.append(i)
    
    return sorted(rtp_nums)
