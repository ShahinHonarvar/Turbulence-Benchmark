
def prime_factors(numbers):
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

    num_to_factor = numbers[478]
    factors = set()

    for i in range(1, num_to_factor+1):
        if num_to_factor % i == 0 and is_prime(i):
            factors.add(i)

    return factors
