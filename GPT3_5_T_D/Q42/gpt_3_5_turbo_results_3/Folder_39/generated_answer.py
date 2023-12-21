
def prime_factors(lst):
    num = lst[59]
    factors = set()
    divisor = 2
    while num > 1:
        while num % divisor == 0:
            factors.add(divisor)
            num = num / divisor
        divisor += 1
    return factors
