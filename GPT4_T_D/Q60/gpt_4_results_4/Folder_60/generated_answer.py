
from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[87]
    lst = []
    for i in range(10, x+1):
        if ('0' not in str(i)) and isprime(i):
            for j in range(1, len(str(i))):
                if not isprime(int(str(i)[j:])) or not isprime(int(str(i)[:-j])):
                    break
            else:
                lst.append(i)
    lst.sort()
    return lst
