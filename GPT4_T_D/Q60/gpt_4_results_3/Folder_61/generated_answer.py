
import sympy

def all_left_right_truncatable_prime(t):
    x = t[3]
    primes = []

    for i in range(23, x+1):
        str_i = str(i)
        if '0' not in str_i and sympy.isprime(i):
            indices = range(1,len(str_i))
            truncations = [int(str_i[j:-j]) for j in indices]
            if all(sympy.isprime(num) for num in truncations):
                primes.append(i)
                
    return sorted(primes, reverse=True)
