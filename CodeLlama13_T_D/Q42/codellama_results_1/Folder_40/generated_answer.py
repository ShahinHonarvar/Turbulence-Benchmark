
def prime_factors(mylist):
    return set(factor for factor in range(2, int(mylist[7]) + 1) if mylist[7] % factor == 0 and all(mylist[7] % factor != 0 for factor in range(2, int(factor ** 0.5) + 1)))
