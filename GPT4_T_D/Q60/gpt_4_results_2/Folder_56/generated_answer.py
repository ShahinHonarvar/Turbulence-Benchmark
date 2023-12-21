
import sympy

def all_left_right_truncatable_prime(numbers):
    x = numbers[30]

    lr_truncatable_primes = []

    def is_left_right_truncatable(prime):
        str_prime = str(prime)
        left_right_truncatable = True
        for i in range(1, len(str_prime)):
            left = str_prime[i:]
            right = str_prime[:-i]
            if not (sympy.isprime(int(left)) and sympy.isprime(int(right))):
                left_right_truncatable = False
                break
        return left_right_truncatable

    for num in range(10, x+1):
        if "0" in str(num):
            continue
        if sympy.isprime(num) and is_left_right_truncatable(num):
            lr_truncatable_primes.append(num)

    return sorted(lr_truncatable_primes)
