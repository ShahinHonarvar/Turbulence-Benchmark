
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        while len(str(n)) > 1:
            n = int(str(n)[1:])
            if not is_prime(n):
                return False
        return True

    x = numbers[24]
    truncatable_primes = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes)
