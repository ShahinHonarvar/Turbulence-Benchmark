
def all_right_truncatable_prime(tup):
    from sympy import isprime

    def is_right_truncatable_prime(num):
        while num > 0:
            if not isprime(num):
                return False
            num = num // 10
        return True

    x = tup[85]
    return sorted([num for num in range(2, x) if is_right_truncatable_prime(num)])
