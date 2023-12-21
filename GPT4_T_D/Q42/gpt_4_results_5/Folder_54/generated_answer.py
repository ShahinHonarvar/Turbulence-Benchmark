
def prime_factors(integers):
    number = integers[51]
    factors = set()
    divisor = 2
    while divisor*divisor <= number:
        if number % divisor:
            divisor += 1
        else:
            number //= divisor
            factors.add(divisor)
    if number > 1:
        factors.add(number)
    return factors
