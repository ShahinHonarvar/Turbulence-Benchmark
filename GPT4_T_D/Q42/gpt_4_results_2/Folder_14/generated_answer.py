
def prime_factors(numbers):
    num = numbers[17]
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
