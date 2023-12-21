
def prime_factors(numbers):
    return set([p for n in numbers[28] for p in range(2, int(n**0.5) + 1) if n % p == 0])
