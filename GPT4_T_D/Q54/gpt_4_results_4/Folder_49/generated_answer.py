
from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[14]
    ans = []
    
    def is_right_truncatable_prime(n):
        n = str(n)
        for i in range(len(n)):
            if not isprime(int(n[i:])):
                return False
        return True

    for i in range(2, x):
        if is_right_truncatable_prime(i):
            ans.append(i)
    return sorted(ans)
