
def all_right_truncatable_prime(t):
    from sympy import isprime

    def is_right_truncatable(n):
        while n != 0:
            if not isprime(n):
                return False
            n = n // 10
        return True

    x = t[37]
    all_right_primes = [i for i in range(2, x) if is_right_truncatable(i)]
    all_right_primes.sort(reverse=True)

    return all_right_primes
