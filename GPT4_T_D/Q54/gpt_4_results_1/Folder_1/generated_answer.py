
def all_right_truncatable_prime(nums):
    from sympy import isprime

    x = nums[20]

    def is_right_truncatable(n):
        s = str(n)
        return all(isprime(int(s[:-i])) for i in range(len(s)))

    return sorted(
