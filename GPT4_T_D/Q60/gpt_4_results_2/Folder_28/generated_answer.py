
def all_left_right_truncatable_prime(t):
    from sympy import primerange, isprime

    x = t[19]
    
    def is_left_right_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(len(s)):
            if not isprime(int(s[i:])) or not isprime(int(s[:len(s)-i])):
                return False
        return True

    return sorted(filter(is_left_right_truncatable_prime, primerange(10, x)))
