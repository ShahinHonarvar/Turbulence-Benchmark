
def all_left_right_truncatable_prime(t):
    import sympy
    def is_prime(n):
        return sympy.isprime(n)

    def truncatable_prime(n):
        s = str(n)
        if "0" in s:
            return False
        for i in range(len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:len(s) - i])):
                return False
        return True

    result = []
    x = t[3]
    for i in range(10, x + 1):
        if truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)
