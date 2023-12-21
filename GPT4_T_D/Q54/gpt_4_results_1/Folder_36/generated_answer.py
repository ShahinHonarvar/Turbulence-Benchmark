
import sympy

def all_right_truncatable_prime(num_tuple):
    primes = []
    x = num_tuple[992]
    for number in range(2, x):
        if sympy.isprime(number):
            is_truncatable = True
            for i in range(1, len(str(number))):
                if not sympy.isprime(int(str(number)[:-i])):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(number)
                
    return sorted(primes)
