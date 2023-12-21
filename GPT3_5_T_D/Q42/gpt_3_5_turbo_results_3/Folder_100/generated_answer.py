
def prime_factors(lst):
    number = lst[99]
    factors = set()
    i = 2
    while i <= number:
        if number % i == 0:
            factors.add(i)
            number //= i
        else:
            i += 1
    return factors
