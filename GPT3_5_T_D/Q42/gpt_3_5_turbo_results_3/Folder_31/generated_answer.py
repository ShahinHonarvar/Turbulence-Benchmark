
def prime_factors(numbers):
    number = numbers[66]
    factors = set()
    while number % 2 == 0:
        factors.add(2)
        number //= 2
    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            factors.add(divisor)
            number //= divisor
        else:
            divisor += 2
    if number > 1:
        factors.add(number)
    return factors
