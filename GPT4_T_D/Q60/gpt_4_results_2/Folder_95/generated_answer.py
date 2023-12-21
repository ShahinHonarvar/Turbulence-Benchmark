
def all_left_right_truncatable_prime(nums):
    import sympy

    def check_prime(n):
        return sympy.isprime(n)

    def check_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not check_prime(int(str_n[i:])) or not check_prime(int(str_n[:len(str_n)-i])):
                return False
        return True

    x = nums[77]
    truncatable = []
    for i in range(10, x+1):
        if check_prime(i) and check_truncatable(i):
            truncatable.append(i)
    return sorted(truncatable)
