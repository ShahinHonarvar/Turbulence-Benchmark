
from sympy import primerange


def all_left_right_truncatable_prime(numbers):
    def is_left_and_right_truncatable_prime(num):
        num = str(num)
        for i in range(len(num)):
            if str(num[i:]) not in primes or str(num[:-i]) not in primes:
                return False
        return True

    x = numbers[35]
    primes = set(map(str, list(primerange(0, x + 1))))
    truncatable_primes = [int(i) for i in primes if '0' not in i and is_left_and_right_truncatable_prime(i)]
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
