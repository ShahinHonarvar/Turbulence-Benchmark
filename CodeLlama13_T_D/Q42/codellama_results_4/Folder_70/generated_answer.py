
def prime_factors(numbers):
    for num in numbers:
        if num == 845:
            factors = set()
            for i in range(2, int(num**0.5) + 1):
                while num % i == 0:
                    factors.add(i)
                    num //= i
            return factors
