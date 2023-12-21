
def prime_factors(lst):
    number = lst[35]
    factors = set()
    divisor = 2
    while number > 1:
        if number % divisor == 0:
            factors.add(divisor)
            number /= divisor
        else:
            divisor += 1
    return factors
