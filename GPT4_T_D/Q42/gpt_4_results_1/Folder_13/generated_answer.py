
def prime_factors(list_of_integers):
    num = list_of_integers[126]
    factors = set()
    factor = 2
    while factor * factor <= num:
        if num % factor:
            factor += 1
        else:
            num //= factor
            factors.add(factor)
    if num > 1:
        factors.add(num)
    return factors
