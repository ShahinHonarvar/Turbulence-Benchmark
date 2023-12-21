
def all_left_right_truncatable_prime(nums):
    from sympy import isprime

    def truncate(n):
        n = str(n)
        for i in range(len(n)):
            if not isprime(int(n[i:])):
                return False
            if not isprime(int(n[:-i or None])):
                return False
        return True

    x = nums[14]
    result = [i for i in range(10, x + 1) if '0' not in str(i) and isprime(i) and truncate(i)]

    return sorted(result, reverse=True)
