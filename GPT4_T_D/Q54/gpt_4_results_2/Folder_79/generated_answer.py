
def all_right_truncatable_prime(tup):
    from sympy import isprime
    def is_right_truncatable_prime(n):
        s = str(n)
        return all(isprime(int(s[:i])) for i in range(1, len(s) + 1))

    x = tup[91]
    return sorted(filter(is_right_truncatable_prime, range(2, x)))
