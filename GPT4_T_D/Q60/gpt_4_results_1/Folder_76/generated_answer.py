
def all_left_right_truncatable_prime(t):
    import sympy
    def is_left_right_truncatable(n):
        s = str(n)
        if '0' in s: return False
        for i in range(len(s)):
            if not sympy.isprime(int(s[i:])) or not sympy.isprime(int(s[:len(s) - i])):
                return False
        return True
    x = t[370]
    return sorted([n for n in range(11, x + 1) if is_left_right_truncatable(n)], reverse=True)
