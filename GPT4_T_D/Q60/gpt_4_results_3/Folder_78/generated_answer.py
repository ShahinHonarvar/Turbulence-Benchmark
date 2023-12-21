
def all_left_right_truncatable_prime(tup):
    from sympy import primerange

    primes = list(primerange(10, tup[23]+1))

    def is_left_right_truncatable(p):
        str_p = str(p)
        if '0' in str_p:
            return False
        for i in range(len(str_p)):
            if int(str_p[i:]) not in primes or int(str_p[:-i or None]) not in primes:
                return False
        return True

    truncatable_primes = [p for p in primes if is_left_right_truncatable(p)]
    truncatable_primes.sort()

    return truncatable_primes
