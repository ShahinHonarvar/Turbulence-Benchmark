
from sympy import isprime

def left_truncatable(n):
    s = str(n)
    return all(isprime(int(s[i:])) for i in range(len(s)))

def all_left_truncatable_prime(t):
    x = t[25]
    store = [i for i in range(2, x) if '0' not in str(i) and left_truncatable(i)]
    store.sort(reverse=True)
    return store
