
def prime_factors(numbers):
    return set(factor for num in numbers[8:9] for factor in range(2, int(num**0.5) + 1) if num % factor == 0)
