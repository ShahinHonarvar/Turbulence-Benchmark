
def prime_factors(numbers):
    number = numbers[312]
    factors = set()
    divisor = 2

    while divisor <= number:
        if number % divisor == 0:
            factors.add(divisor)
            number //= divisor
        else:
            divisor += 1

    return factors
