
def all_left_right_truncatable_prime(tup):
    import sympy

    def left_right_truncatable(prime):
        str_prime = str(prime)
        if '0' in str_prime:
            return False
        len_prime = len(str_prime)
        for i in range(len_prime):
            left_removed = int(str_prime[i:])
            right_removed = int(str_prime[:len_prime - i])
            if not sympy.isprime(left_removed) or not sympy.isprime(right_removed):
                return False
        return True

    results = []
    for i in range(2, tup[23] + 1):
        if sympy.isprime(i) and left_right_truncatable(i):
            results.append(i)

    return sorted(results)
