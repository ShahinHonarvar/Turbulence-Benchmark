
def prime_factors(lst):
    number = lst[828]
    factors = set()
    div = 2
    while number > 1:
        if number % div == 0:
            factors.add(div)
            number = number // div
        else:
            div += 1
    return factors
