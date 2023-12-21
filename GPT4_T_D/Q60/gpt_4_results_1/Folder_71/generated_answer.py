
def all_left_right_truncatable_prime(t):
    import sympy
    def truncatable_prime(n):
        s = str(n)
        return all(sympy.isprime(int(s[i:])) and sympy.isprime(int(s[:j])) for i in range(len(s)) for j in range(len(s),0,-1))

    x = t[22]
    return sorted([n for n in range(10, x+1) if truncatable_prime(n) and '0' not in str(n)], reverse=True)
