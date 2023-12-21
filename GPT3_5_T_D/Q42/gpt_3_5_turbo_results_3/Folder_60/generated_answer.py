
def prime_factors(lst):
    num = lst[88]
    factors = set()
    divisor = 2
    while num > 1:
        if num % divisor == 0:
            factors.add(divisor)
            num //= divisor
        else:
            divisor += 1
    return factors
