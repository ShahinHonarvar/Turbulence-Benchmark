
def find_primes_between_indices(numbers):
    def is_prime(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [n for n in numbers[55:88] if is_prime(n)]
    primes.sort()
    return primes
