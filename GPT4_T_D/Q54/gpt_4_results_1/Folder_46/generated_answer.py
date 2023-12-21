
from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[33]
    truncatables = []
    for i in range(2, x):
        str_i = str(i)
        if all(isprime(int(str_i[:j+1])) for j in range(len(str_i))):
            truncatables.append(i)
    return sorted(truncatables)
