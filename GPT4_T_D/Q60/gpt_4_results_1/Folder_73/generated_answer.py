
def all_left_right_truncatable_prime(t):
    from sympy import isprime
    x = t[97]

    def is_left_right_truncatable(p):
        p = str(p)
        if '0' in p:
            return False
        for i in range(len(p)):
            if not (isprime(int(p[i:])) and isprime(int(p[:len(p) - i]))):
                return False
        return True

    return sorted([i for i in range(10, x + 1) if isprime(i) and is_left_right_truncatable(i)])
