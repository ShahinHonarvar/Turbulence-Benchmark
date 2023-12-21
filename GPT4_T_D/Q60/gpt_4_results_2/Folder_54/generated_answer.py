
import sympy

def all_left_right_truncatable_prime(tup):
    x = tup[88]
    primes = []
    def is_left_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not sympy.isprime(int(str_n[i:])):
                return False
        return True
    def is_right_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n), 0, -1):
            if not sympy.isprime(int(str_n[:i])):
                return False
        return True
    for number in range(10, x + 1):
        if '0' not in str(number) and is_left_truncatable_prime(number) and is_right_truncatable_prime(number):
            primes.append(number)
    return sorted(primes, reverse=True)
