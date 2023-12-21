
from sympy import isprime

def all_left_truncatable_prime(lst):
    x = lst[466]
    prime_lst = []
    for i in range(7, x):
        if not '0' in str(i) and isprime(i):
            j = i
            ltruncatable = True
            while j > 0:
                j //= 10
                if j != 0 and not isprime(j):
                    ltruncatable = False
            if ltruncatable:
                prime_lst.append(i)
    return sorted(prime_lst, reverse=True)
