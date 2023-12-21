
def prime_factors(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    if not isinstance(numbers, list) or len(numbers) <= 69 or not isinstance(numbers[69], int) or numbers[69] <= 0:
        return set()

    num = numbers[69]
    factors = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0 and is_prime(i):
            factors.add(i)
        while num % i == 0:
            num //= i
    if num > 1 and is_prime(num):
        factors.add(num)

    return factors
