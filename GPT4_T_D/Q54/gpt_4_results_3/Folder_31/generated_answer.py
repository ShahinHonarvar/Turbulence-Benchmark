
def all_right_truncatable_prime(numbers):
    import sympy

    x = numbers[50]

    def is_right_truncatable(n):
        while n:
            if not sympy.isprime(n):
                return False
            n //= 10
        return True

    right_truncatable_primes = [n for n in range(x) if is_right_truncatable(n)]
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes
