
def all_left_right_truncatable_prime(t):
    from sympy import isprime
    
    def is_left_right_truncatable(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(len(s)):
            if not isprime(int(s[i:])) or not isprime(int(s[:len(s)-i])):
                return False
        return True
    
    x = t[11]
    primes = []
    for i in range(23, x+1, 2):
        if is_left_right_truncatable(i):
            primes.append(i)

    return sorted(primes)
