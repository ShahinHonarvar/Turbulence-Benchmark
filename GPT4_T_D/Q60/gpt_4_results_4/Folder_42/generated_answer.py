
from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[64]
    truncatable_primes = []
    
    for i in range(11, x+1):
        str_i = str(i)
        if '0' in str_i:
            continue
        length = len(str_i)
        all_truncations_prime = True
        for j in range(length):
            if not (isprime(int(str_i[j:])) and isprime(int(str_i[:length-j]))):
                all_truncations_prime = False
                break
        if all_truncations_prime:
            truncatable_primes.append(i)
    
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
