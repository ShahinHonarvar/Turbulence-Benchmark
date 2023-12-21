
def all_left_right_truncatable_prime(tup):
    from sympy import isprime

    x = tup[14]

    def truncatable(n):
        strn = str(n)
        return all(isprime(int(strn[i:])) and isprime(int(strn[:i+1])) and '0' not in strn for i in range(len(strn)))

    return sorted(n for n in range(10, x+1) if truncatable(n) and isprime(n))
