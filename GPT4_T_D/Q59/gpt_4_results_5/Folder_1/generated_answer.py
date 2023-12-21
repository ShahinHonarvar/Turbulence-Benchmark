
def all_left_truncatable_prime(nums):
    from sympy import isprime

    def is_left_truncatable(n):
        str_n = str(n)

        if '0' in str_n:
            return False

        return all(isprime(int(str_n[i:])) for i in range(len(str_n)))

    x = nums[20]

    left_truncatable_primes = [i for i in range(2, x) if is_left_truncatable(i)]

    return sorted(left_truncatable_primes, reverse=True)
