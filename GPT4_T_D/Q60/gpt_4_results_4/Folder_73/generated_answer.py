
def all_left_right_truncatable_prime(tup):
    import sympy

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False

        for i in range(1, len(str(n))):
            if not(sympy.isprime(int(str(n)[i:])) and sympy.isprime(int(str(n)[:-i]))):
                return False
        return True

    x = tup[97]
    result = []
    for i in range(10, x+1):
        if sympy.isprime(i) and is_left_right_truncatable(i):
            result.append(i)
    return sorted(result)
