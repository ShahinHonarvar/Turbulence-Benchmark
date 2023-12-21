
def all_right_truncatable_prime(tup):
    from sympy import isprime

    def check_right_truncatable(num):
        while num:
            if not isprime(num):
                return False
            num //= 10
        return True

    x = tup[177]
    return sorted(p for p in range(x) if check_right_truncatable(p))
