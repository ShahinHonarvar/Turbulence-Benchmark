
def all_left_right_truncatable_prime(nums):
    import sympy
    def is_truncatable(n):
        if '0' in str(n):
            return False
        str_n = str(n)
        l = len(str_n)
        for i in range(l):
            if not sympy.isprime(int(str_n[i:])):
                return False
            if not sympy.isprime(int(str_n[:l - i])):
                return False
        return True
    x = nums[46]
    result = []
    for num in range(11, x + 1, 2):
        if is_truncatable(num):
            result.append(num)
    return sorted(result, reverse=True)
