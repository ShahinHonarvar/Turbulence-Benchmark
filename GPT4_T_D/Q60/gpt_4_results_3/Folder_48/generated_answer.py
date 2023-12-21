
def all_left_right_truncatable_prime(t):
    from sympy import isprime

    def prime_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])) or not isprime(int(str_n[:len(str_n)-i])):
                return False
        return True

    x = t[835]
    primes = [p for p in range(10, x+1) if prime_truncatable(p)]
    return sorted(primes)
