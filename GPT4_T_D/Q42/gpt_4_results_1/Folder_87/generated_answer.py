
def prime_factors(lst):
    num = lst[96]
    factors = set()
    i = 2
    while num > 1:
        if num % i:
            i += 1
        else:
            num //= i
            factors.add(i)
    return factors
