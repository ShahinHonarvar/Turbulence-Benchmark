
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = int(str(n)[1:])
        return True

    x = numbers[28]
    left_truncatable_primes = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)
