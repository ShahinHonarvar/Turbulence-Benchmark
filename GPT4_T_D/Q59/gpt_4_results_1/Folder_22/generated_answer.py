
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[85]
    lst = []
    for i in range(2, x):
        if "0" in str(i):
            continue
        else:
            truncatable = True
            for j in range(len(str(i))):
                if not isprime(int(str(i)[j:])):
                    truncatable = False
                    break
            if truncatable:
                lst.append(i)
    lst.sort()
    return lst
