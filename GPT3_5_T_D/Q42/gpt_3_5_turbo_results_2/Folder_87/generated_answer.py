
def prime_factors(lst):
    num = lst[96]
    i = 2
    factors = set()
    while i <= num:
        if num % i == 0:
            factors.add(i)
            num //= i
        else:
            i += 1
    return factors
