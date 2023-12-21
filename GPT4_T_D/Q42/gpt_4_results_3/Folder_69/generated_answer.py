
def prime_factors(list_of_integers):
    number = list_of_integers[459]
    factors = set()
    div = 2
    while div * div <= number:
        if number % div:
            div += 1
        else:
            number //= div
            factors.add(div)
    if number > 1:
        factors.add(number)
    return factors
