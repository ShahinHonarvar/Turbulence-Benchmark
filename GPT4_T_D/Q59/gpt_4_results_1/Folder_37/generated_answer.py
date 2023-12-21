
def all_left_truncatable_prime(nums):
    import sympy

    def is_truncatable(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        for i in range(1, len(str_num)):
            if not sympy.isprime(int(str_num[i:])):
                return False
        return True

    x = nums[35]
    prime_nums = [i for i in range(2, x) if sympy.isprime(i)]
    left_truncatable_nums = [i for i in prime_nums if is_truncatable(i)]
    
    return sorted(left_truncatable_nums, reverse=True)
