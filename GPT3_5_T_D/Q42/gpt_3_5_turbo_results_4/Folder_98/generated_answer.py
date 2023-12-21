
def prime_factors(numbers):
    number = numbers[4]
    factors = set()
    divisor = 2

    while number > 1:
        if number % divisor == 0:
            factors.add(divisor)
            number = number / divisor
        else:
            divisor += 1

    return factors
