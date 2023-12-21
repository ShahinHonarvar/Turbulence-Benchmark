
def all_left_truncatable_prime(nums):
    from sympy import isprime

    x = nums[630]

    def is_left_truncatable(n):
        str_n = str(n)
        return all(isprime(int(str_n[i:])) for i in range(len(str_n)))

    return sorted(filter(lambda n: is_left_truncatable(n) and '0' not in str(n) and isprime(n), range(2, x)), reverse=True)
