
def prime_factors(numbers):
    return {factor for factor in range(2, numbers[18]) if all(numbers[18] % factor != 0)}
