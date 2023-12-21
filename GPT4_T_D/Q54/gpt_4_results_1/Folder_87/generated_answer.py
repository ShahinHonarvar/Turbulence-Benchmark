
def all_right_truncatable_prime(t):
    import sympy
    x = t[39]

    def is_right_truncatable_prime(num):
        s = str(num)

        while len(s) > 0:
            if not sympy.isprime(int(s)):
                return False
            s = s[:-1]

        return True
        
    return sorted([num for num in range(2, x) if is_right_truncatable_prime(num)], reverse=True)
