
def prime_factors(lst):
    num = lst[34]
    prime_factors = set()

    factor = 2
    while factor * factor <= num:
        if num % factor:
            factor += 1
        else:
            num //= factor
            prime_factors.add(factor)
    if num > 1:
        prime_factors.add(num)
        
    return prime_factors
