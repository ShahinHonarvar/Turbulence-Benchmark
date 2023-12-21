
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[760]

    def is_truncatable_prime(num):
        num_str = str(num)
        for i in range(len(num_str)):
            if not isprime(int(num_str[i:])) or not isprime(int(num_str[:len(num_str)-i])) or '0' in num_str:
                return False
        return True

    truncatable_primes = [i for i in range(10, x + 1) if is_truncatable_prime(i)]
    truncatable_primes.sort(reverse=True)

    return truncatable_primes
