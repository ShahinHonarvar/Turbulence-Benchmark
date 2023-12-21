
def prime_factors(numbers):
    integer = numbers[83]
    factors = set()
    divisor = 2
    while integer > 1:
        if integer % divisor == 0:
            factors.add(divisor)
            integer /= divisor
        else:
            divisor += 1
    return factors
