
def all_left_truncatable_prime(t):
    from sympy import isprime

    x = t[835]

    def is_left_truncatable_prime(n):
        n = str(n)
        if '0' in n:
            return False
        return all(isprime(int(n[i:])) for i in range(len(n)))

    return sorted(filter(is_left_truncatable_prime, range(2, x)))
