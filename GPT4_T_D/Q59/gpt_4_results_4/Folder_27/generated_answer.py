
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[79]
    truncatable_primes = []
    l_truncatable = lambda prime_list : all(isprime(int(prime_list[i:])) for i in range(len(prime_list)))

    for i in range(1, x):
        prime_str = str(i)
        if '0' not in prime_str and isprime(i) and l_truncatable(prime_str):
            truncatable_primes.append(i)
    
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
