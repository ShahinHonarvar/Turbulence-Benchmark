
def all_right_truncatable_prime(nums):
    from sympy import isprime
    x = nums[65]

    def is_right_truncatable_prime(n):
        n = str(n)
        for i in range(len(n)):
            if not isprime(int(n[i:])):
                return False
        return True

    return sorted([i for i in range(10, x) if is_right_truncatable_prime(i)], reverse=True)
