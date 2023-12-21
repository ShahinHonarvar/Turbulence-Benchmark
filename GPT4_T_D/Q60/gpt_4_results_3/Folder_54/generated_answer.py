
def all_left_right_truncatable_prime(nums):
    import sympy

    x = nums[88]
    truncatable_primes = []

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not sympy.isprime(int(str(n)[i:])) or not sympy.isprime(int(str(n)[:len(str(n))-i])):
                return False
        return True

    for i in range(11, x + 1, 2):
        if is_left_right_truncatable(i):
            truncatable_primes.append(i)

    return sorted(truncatable_primes, reverse=True)
