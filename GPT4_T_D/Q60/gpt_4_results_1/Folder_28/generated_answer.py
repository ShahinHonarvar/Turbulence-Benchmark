
def all_left_right_truncatable_prime(t):
    from sympy import isprime
    
    def left_right_truncatable(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(len(s)):
            if not isprime(int(s[i:])) or not isprime(int(s[:len(s) - i])):
                return False
        return True

    x = t[19]
    result = [i for i in range(11, x + 1) if left_right_truncatable(i)]
    return sorted(result)
