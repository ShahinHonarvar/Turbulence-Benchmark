
def all_right_truncatable_prime(t):
    from sympy import isprime
    def right_truncatable_prime(n):
        return all(isprime(int(str(n)[:i])) for i in range(len(str(n)), 0, -1))

    x = t[18]
    return sorted([i for i in range(2, x) if right_truncatable_prime(i)], reverse=True)
