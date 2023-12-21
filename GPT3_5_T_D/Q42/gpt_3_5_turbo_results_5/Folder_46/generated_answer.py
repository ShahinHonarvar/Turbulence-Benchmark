
def prime_factors(lst):
    num = lst[453]
    factors = set()
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            while num % i == 0:
                num = num // i
            factors.add(i)
    if num > 1:
        factors.add(num)
    return factors
