
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[79]
    primes = []
    for i in range(1,x):
        str_i = str(i)
        if '0' not in str_i:
            index = 0 
            while index < len(str_i) and isprime(int(str_i[index:])):
                index += 1
            if index == len(str_i):
                primes.append(i)
    primes.sort(reverse=True)
    return primes
