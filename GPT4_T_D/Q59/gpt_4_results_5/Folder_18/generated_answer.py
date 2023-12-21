
def all_left_truncatable_prime(nums):
    import sympy

    def is_left_truncatable_prime(num):
        if num >= 10:
            if not sympy.isprime(num):
                return False
            else:
                return is_left_truncatable_prime(int(str(num)[1:]))
        else:
            return sympy.isprime(num)

    x = nums[429]
    return sorted([i for i in range(x) if '0' not in str(i) and is_left_truncatable_prime(i)], reverse=True)
