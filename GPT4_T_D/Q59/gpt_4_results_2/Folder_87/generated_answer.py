
def all_left_truncatable_prime(nums):
    import sympy

    x = nums[39]
    primes = [str(p) for p in sympy.primerange(10, x) if '0' not in str(p)]
    left_truncatable_primes = [p for p in primes if all(sympy.isprime(int(p[i:])) for i in range(len(p)))]

    left_truncatable_primes = [int(i) for i in left_truncatable_primes]
    return sorted(left_truncatable_primes, reverse=True)
