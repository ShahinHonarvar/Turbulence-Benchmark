
def prime_factors(lst):
    num = lst[73]
    factors = set()
    divisor = 2
    while divisor <= num:
        if num % divisor:
            divisor += 1
        else:
            num //= divisor
            factors.add(divisor)
    return factors
