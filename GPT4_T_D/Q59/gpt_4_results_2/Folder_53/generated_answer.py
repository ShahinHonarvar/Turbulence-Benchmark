
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[86]

    def check_left_truncatable(num):
        if '0' in str(num):
            return False
        for i in range(1, len(str(num))):
            if not isprime(int(str(num)[i:])):
                return False
        return True

    left_truncatable_primes = [i for i in range(10, x) if isprime(i) and check_left_truncatable(i)]
    left_truncatable_primes.sort(reverse=True)

    return left_truncatable_primes
