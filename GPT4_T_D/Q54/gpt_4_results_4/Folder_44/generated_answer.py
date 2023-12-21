
import sympy

def all_right_truncatable_prime(numbers):
    x = numbers[39]
    right_truncatable_primes = []
    for i in range(2, x):
        str_num = str(i)
        for j in range(len(str_num)):
            if not sympy.isprime(int(str_num[j:])):
                break
        else:
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)
