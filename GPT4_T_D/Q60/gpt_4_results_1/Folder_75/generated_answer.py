
def all_left_right_truncatable_prime(nums):
    from sympy import isprime

    x = nums[41]

    def is_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not (isprime(int(str_n[i:])) and isprime(int(str_n[:len(str_n)-i]))):
                return False
        return True

    truncatable_primes = [i for i in range(10, x+1) if is_truncatable(i)]
    return sorted(truncatable_primes)
