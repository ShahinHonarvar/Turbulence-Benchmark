
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(p):
        while p > 0:
            if not is_prime(p):
                return False
            p //= 10
        return True

    x = numbers[37]
    right_truncatable_primes = []
    for n in range(2, x):
        if is_right_truncatable(n):
            right_truncatable_primes.append(n)

    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes
