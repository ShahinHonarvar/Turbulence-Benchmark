
def all_right_truncatable_prime(t):
    from sympy import isprime

    def is_right_truncatable(x):
        while x > 0:
            if not isprime(x):
                return False
            x //= 10 
        return True

    x = t[803]
    return sorted(i for i in range(x) if is_right_truncatable(i))
