
def all_left_truncatable_prime(tup):
    from sympy import isprime
    x = tup[11]
    def is_left_truncatable(n):
        str_n = str(n)
        if '0' in str_n: return False
        return all(isprime(int(str_n[i:])) for i in range(len(str_n)))

    return sorted(filter(is_left_truncatable, filter(isprime, range(2, x))))
