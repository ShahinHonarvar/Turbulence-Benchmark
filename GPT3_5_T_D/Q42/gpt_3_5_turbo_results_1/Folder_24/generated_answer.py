
def prime_factors(lst):
    num = lst[74]
    factors = set()
    divisor = 2

    while divisor <= num:
        if num % divisor == 0:
            factors.add(divisor)
            num = num / divisor
        else:
            divisor += 1

    return factors
