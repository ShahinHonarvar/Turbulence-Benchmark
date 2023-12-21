
def prime_factors(numbers):
    number = numbers[85]
    factors = set()
    factor = 2

    while factor * factor <= number:
        if number % factor == 0:
            number //= factor
            factors.add(factor)
        else:
            factor += 1
            
    if number > 1:
        factors.add(number)

    return factors
