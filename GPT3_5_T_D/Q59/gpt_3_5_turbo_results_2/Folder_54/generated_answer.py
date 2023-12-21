
import sympy

def all_left_truncatable_prime(numbers):
    x = numbers[88]
    primes = []
    for i in range(2, x):
        if '0' not in str(i):
            truncatable = True
            for j in range(len(str(i))):
                if not sympy.isprime(int(str(i)[j:])):
                    truncatable = False
                    break
            if truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)
