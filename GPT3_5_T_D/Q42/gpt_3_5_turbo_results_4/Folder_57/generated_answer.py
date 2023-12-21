
def prime_factors(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    index_92 = numbers[92]
    factors = set()
    for i in range(2, int(index_92 ** 0.5) + 1):
        if index_92 % i == 0 and is_prime(i):
            factors.add(i)
        if index_92 % i == 0 and is_prime(index_92 // i):
            factors.add(index_92 // i)
    return factors
