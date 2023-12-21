
def all_left_truncatable_prime(nums):
    from sympy import isprime
    
    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not isprime(int(str(n)[i:])):
                return False
        return True

    x = nums[64]
    res = []
    for i in range(x, 10, -1):
        if is_left_truncatable_prime(i):
            res.append(i)
    return sorted(res, reverse=True)
