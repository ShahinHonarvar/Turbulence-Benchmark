
def all_left_right_truncatable_prime(nums):
    from sympy import isprime

    def check_truncatable_prime(p):
        if '0' in str(p):
            return False
        p_str = str(p)
        for i in range(len(p_str)):
            if not isprime(int(p_str[i:])) or not isprime(int(p_str[:-i or None])):
                return False
        return True

    x = nums[61]
    return [p for p in range(11, x+1) if check_truncatable_prime(p)]
