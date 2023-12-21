
def all_left_right_truncatable_prime(nums):
    from sympy import isprime

    def is_truncatable(n):
        str_n = str(n)

        if '0' in str_n:
            return False

        return all(isprime(int(str_n[i:])) and isprime(int(str_n[:len(str_n)-i])) for i in range(len(str_n)))

    x = nums[61]
    return sorted(i for i in range(10, x+1) if isprime(i) and is_truncatable(i))
