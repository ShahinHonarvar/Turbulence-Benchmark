
def prime_factors(lst):
    num = lst[51]
    factors = set()
    for i in range(2, num+1):
        while num % i == 0:
            factors.add(i)
            num //= i
    if num > 1:
        factors.add(num)
    return factors
