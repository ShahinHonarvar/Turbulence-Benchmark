
import math

def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[29]
    truncatable_primes = []

    for i in range(x - 1, 1, -1):
        num = str(i)
        is_truncatable = True

        while num != '':
            if not is_prime(int(num)):
                is_truncatable = False
                break
            num = num[:-1]

        if is_truncatable:
            truncatable_primes.append(i)

    return sorted(truncatable_primes, reverse=True)
