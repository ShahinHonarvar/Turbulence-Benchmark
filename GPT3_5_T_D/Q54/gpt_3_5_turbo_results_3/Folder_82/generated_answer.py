
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[69]
    right_truncatable_primes = []

    def is_right_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    for i in range(x - 1, 1, -1):
        if is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)

    return sorted(right_truncatable_primes, reverse=True)
