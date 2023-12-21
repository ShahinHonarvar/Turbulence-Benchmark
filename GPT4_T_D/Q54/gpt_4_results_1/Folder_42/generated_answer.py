
def all_right_truncatable_prime(t):
    from sympy import isprime

    def is_right_truncatable_prime(n):
        s = str(n)
        return all(isprime(int(s[:i])) for i in range(len(s), 0, -1))

    x = t[64]
    truncatable_primes = [i for i in range(x) if is_right_truncatable_prime(i)]
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
