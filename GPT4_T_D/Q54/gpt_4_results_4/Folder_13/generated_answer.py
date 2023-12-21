
def all_right_truncatable_prime(t):
    from sympy import isprime

    def is_rtp(n):
        n = str(n)
        return all(isprime(int(n[:i])) for i in range(1, len(n) + 1))

    x = t[784]
    return sorted([i for i in range(2, x) if is_rtp(i)])
