
def prime_factors(numbers):
    return set(factor for factor in range(2, numbers[74]) if all(number % factor != 0 for number in numbers))
