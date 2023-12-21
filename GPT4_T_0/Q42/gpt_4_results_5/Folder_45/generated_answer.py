
def prime_factors(lst):
    num = lst[33]
    factors = set()
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.add(i)
    if num > 1:
        factors.add(num)
    return factors
