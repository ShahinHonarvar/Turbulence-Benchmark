
def all_left_right_truncatable_prime(nums):
    import sympy

    def is_truncatable(p):
        p = str(p)
        if '0' in p:
            return False

        for i in range(1, len(p)):
            if not (sympy.isprime(int(p[i:])) and sympy.isprime(int(p[:-i]))):
                return False

        return True

    x = nums[466]
    primes = [p for p in sympy.primerange(10, x+1) if is_truncatable(p)]
    return sorted(primes, reverse=True)
