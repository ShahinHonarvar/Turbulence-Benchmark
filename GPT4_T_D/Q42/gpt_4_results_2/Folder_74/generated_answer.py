
def prime_factors(numbers):
    number = numbers[48]
    factors = set()
    div = 2

    while number>1:
        if number % div == 0:
            factors.add(div)
            number //= div
        else:
            div += 1

    return factors
