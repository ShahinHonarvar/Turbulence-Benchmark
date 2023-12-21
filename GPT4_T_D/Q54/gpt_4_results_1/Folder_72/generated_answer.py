
from sympy import isprime

def all_right_truncatable_prime(tup):
    x = tup[31]
    right_truncatable_primes =  []

    for num in range(2, x):     
        is_truncatable_prime = True
        num_temp = str(num)

        while len(num_temp) > 0:
            if not isprime(int(num_temp)):
                is_truncatable_prime = False
                break
            num_temp = num_temp[:-1]

        if is_truncatable_prime:
            right_truncatable_primes.append(num)

    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes
