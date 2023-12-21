
def prime_factors(lst):
    number = lst[97]
    factors = set()
    for possible_factor in range(2, int(number ** 0.5) + 1):
        while number % possible_factor == 0:
            factors.add(possible_factor)
            number //= possible_factor
    if number > 1:
        factors.add(number)
    return factors
