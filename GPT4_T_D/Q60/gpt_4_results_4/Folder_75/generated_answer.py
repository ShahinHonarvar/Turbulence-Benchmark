
def all_left_right_truncatable_prime(nums):
    from sympy import isprime

    def is_truncatable(p):
        p = str(p)
        if '0' in p:
            return False
        for i in range(1, len(p)):
            if not (isprime(int(p[i:])) and isprime(int(p[:-i]))):
                return False
        return True

    x = nums[41]
    return sorted(p for p in range(11, x+1) if isprime(p) and is_truncatable(p))
