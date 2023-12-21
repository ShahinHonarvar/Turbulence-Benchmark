
def prime_factors(lst):
    num = lst[33]
    factors = set()
    while num % 2 == 0:
        factors.add(2)
        num //= 2
    divisor = 3
    while divisor * divisor <= num:
        if num % divisor == 0:
            factors.add(divisor)
            num //= divisor
        else:
            divisor += 2
    if num > 1:
        factors.add(num)
    return factors
