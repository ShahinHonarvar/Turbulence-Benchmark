
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[65]

    def is_left_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    left_truncatable_primes = []
    for i in range(10, x):
        if is_left_truncatable(i):
            left_truncatable_primes.append(i)

    return sorted(left_truncatable_primes, reverse=True)
