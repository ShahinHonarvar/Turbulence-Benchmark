
def all_left_truncatable_prime(tuple_x):
    import sympy
    def is_left_truncatable_prime(num):
        if '0' in str(num):
            return False
        for i in range(len(str(num))):
            if not sympy.isprime(int(str(num)[i:])):
                return False
        return True

    x = tuple_x[49]
    return sorted([i for i in range(2, x) if is_left_truncatable_prime(i)])
