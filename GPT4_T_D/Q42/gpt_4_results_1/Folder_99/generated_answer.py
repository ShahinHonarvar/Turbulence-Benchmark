
def prime_factors(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_prime_factors(n):
        primes = set()
        for i in range(2, n + 1):
            if n % i == 0:
                if is_prime(i):
                    primes.add(i)
        return primes

    if 733 >= len(numbers):
        return "Index out of range"
    else:
        return get_prime_factors(numbers[733])
