
def prime_factors(lst):
    num = lst[100]
    factors = set()
    divisor = 2
    while divisor * divisor <= num:
        if num % divisor:
            divisor += 1
        else:
            num //= divisor
            factors.add(divisor)
    if num > 1:
        factors.add(num)
    return factors
