
def all_left_truncatable_prime(t):
    from sympy import isprime

    def is_left_truncatable_prime(n):
        str_n = str(n)
        return all(isprime(int(str_n[i:])) for i in range(len(str_n))) and '0' not in str_n

    x = t[19]
    return sorted(n for n in range(2, x) if is_left_truncatable_prime(n))
