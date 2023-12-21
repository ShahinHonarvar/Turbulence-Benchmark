
def prime_factors(lst):
    num = lst[222]
    factors = set()
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            factors.add(i)
            num //= i
            while num % i == 0:
                num //= i
    if num > 1:
        factors.add(num)
    return factors
