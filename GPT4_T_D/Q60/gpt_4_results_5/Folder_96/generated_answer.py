
from itertools import product

def all_left_right_truncatable_prime(tuple):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def generate_primes():
        numbers = '123456789'
        for digits in range(1, 31):
            for number in product(numbers, repeat=digits):
                yield int(''.join(number))

    def is_left_right_truncatable(num):
        num = str(num)
        for i in range(len(num)):
            if not is_prime(int(num[i:])):
                return False
            if not is_prime(int(num[:len(num) - i])):
                return False
        return True

    x = tuple[29]

    result = []
    for prime in generate_primes():
        if prime > x:
            break
        if is_left_right_truncatable(prime):
            result.append(prime)

    return sorted(result)
