
from sympy import isprime

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[36]
    ltrunc_primes = []

    # Generate all primes less than x
    for num in range(2, x):
        if '0' in str(num):
            continue
        
        num_str = str(num)

        for i in range(len(num_str)):
            if not isprime(int(num_str[i:])):
                break
        else:
            ltrunc_primes.append(num)

    return sorted(ltrunc_primes, reverse=True)
