
import sympy

def all_left_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[43]
    lr_truncatable_primes = []

    for num in range(10, x + 1):
        if '0' not in str(num) and sympy.isprime(num):
            length = len(str(num))
            lr_truncatable = True
            for i in range(length):
                if not (sympy.isprime(int(str(num)[i:])) and sympy.isprime(int(str(num)[:length-i]))):
                    lr_truncatable = False
                    break
            if lr_truncatable:
                lr_truncatable_primes.append(num)
    return sorted(lr_truncatable_primes)
