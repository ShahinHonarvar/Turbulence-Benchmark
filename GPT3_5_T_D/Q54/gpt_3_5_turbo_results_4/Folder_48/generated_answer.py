
import sympy

def all_right_truncatable_prime(numbers):
    x = numbers[835]
    primes = []
    for i in range(x - 1, 10, -1):
        if sympy.isprime(i):
            truncated_prime = True
            num = str(i)
            while len(num) > 1:
                num = num[:-1]
                if not sympy.isprime(int(num)):
                    truncated_prime = False
                    break
            if truncated_prime:
                primes.append(i)
    return sorted(primes)
