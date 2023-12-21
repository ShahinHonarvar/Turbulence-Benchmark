
def all_right_truncatable_prime(numbers):
    x = numbers[94]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(p):
        while p > 0:
            if not is_prime(p):
                return False
            p //= 10
        return True

    right_truncatable_primes = []
    for i in range(x):
        if is_right_truncatable(i):
            right_truncatable_primes.append(i)
    right_truncatable_primes.sort()

    return right_truncatable_primes
