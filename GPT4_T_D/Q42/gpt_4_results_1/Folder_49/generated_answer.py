
def prime_factors(lst):
    number = lst[68]
    factors = []
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            factors.append(i)
    if number > 1:
        factors.append(number)
    return set(factors)
