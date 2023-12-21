
def prime_factors(numbers):
    return set([factor for factor in range(2, 49) if all(number % factor == 0 for number in numbers)])
