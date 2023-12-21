
def all_left_truncatable_prime(tup):
    import sympy as sp

    def is_left_truncatable_prime(n):
        if not sp.isprime(n):
            return False
        n = str(n)
        return all(sp.isprime(int(n[i:])) for i in range(len(n)))

    x = tup[14]
    result = [i for i in range(1, x) if '0' not in str(i) and is_left_truncatable_prime(i)]
    result.sort()
    return result
