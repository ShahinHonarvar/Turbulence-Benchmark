
def all_left_right_truncatable_prime(nums):
    import sympy

    def is_left_right_truncatable(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        for i in range(len(str_num)):
            if not sympy.isprime(int(str_num[i:])):
                return False
            if not sympy.isprime(int(str_num[:len(str_num)-i])):
                return False
        return True

    x = nums[11]
    result = []
    for i in range(10, x + 1):
        if sympy.isprime(i) and is_left_right_truncatable(i):
            result.append(i)

    result.sort()

    return result
