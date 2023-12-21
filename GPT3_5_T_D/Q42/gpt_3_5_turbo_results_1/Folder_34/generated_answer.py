
def prime_factors(lst):
    num = lst[97]
    factors = set()
    i = 2
    while i <= num:
        if num % i == 0:
            factors.add(i)
            num = num // i
        else:
            i += 1
    return factors
