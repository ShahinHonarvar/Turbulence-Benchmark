
def all_right_truncatable_prime(t):
    from sympy import isprime

    def is_right_truncatable_prime(n):
        str_n = str(n)
        return all(isprime(int(str_n[:i])) for i in range(1, len(str_n)+1))

    x = t[433]

    truncatable_primes = [i for i in range(2, x) if is_right_truncatable_prime(i)]

    return sorted(truncatable_primes, reverse=True)
