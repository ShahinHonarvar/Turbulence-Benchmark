
def all_left_right_truncatable_prime(tup):
    import sympy

    x = tup[758]

    def is_left_right_truncatable_prime(n):
        str_n = str(n)

        if '0' in str_n:
            return False

        for i in range(len(str_n)):
            if not sympy.isprime(int(str_n[i:])) or not sympy.isprime(int(str_n[:len(str_n)-i])):
                return False
        return True

    return sorted(filter(is_left_right_truncatable_prime, sympy.primerange(10, x+1)))
