
def find_primes_between_indices(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    primes = []
    if 62 < len(numbers):
        for i in range(25, 63):
            if is_prime(numbers[i]):
                primes.append(numbers[i])
    return sorted(primes)
