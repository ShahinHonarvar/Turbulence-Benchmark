
def prime_factors(lst):
    num = lst[17]
    factors = set()
    i = 2
    while i <= num:
        if num % i == 0:
            factors.add(i)
            num = num / i
            i -= 1
        i += 1
    return factors
