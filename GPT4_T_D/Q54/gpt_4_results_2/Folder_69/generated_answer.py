
from sympy import isprime

def all_right_truncatable_prime(tup):
    x = tup[760]
    def rtp(n):
        if n <= 1:
            return False
        s = str(n)
        for i in range(len(s)):
            if not isprime(int(s[i:])):
                return False
        return True

    result = [i for i in range(1, x) if rtp(i)]
    result.sort(reverse=True)
    return result
