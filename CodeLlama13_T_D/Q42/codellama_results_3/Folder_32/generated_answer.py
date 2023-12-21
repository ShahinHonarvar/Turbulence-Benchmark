
def prime_factors(numbers):
    return {factor for number in numbers[849] for factor in range(2, int(number ** 0.5) + 1) if number % factor == 0}
