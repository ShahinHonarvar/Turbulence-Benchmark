
import sympy

def all_left_truncatable_prime(numbers):
    x = numbers[67]
    primes = []
    for i in range(x-1, 0, -1):
        num = str(i)
        if '0' in num:
            continue
        truncatable = True
        while num != '':
            if not sympy.isprime(int(num)):
                truncatable = False
                break
            num = num[1:]
        if truncatable:
            primes.append(i)
    return primes
