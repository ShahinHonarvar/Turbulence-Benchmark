
def prime_factors(numbers):
    num = numbers[72]
    factors = set()
    p = 2
    while num >= (p * p):
        if (num % p):
            p += 1
        else:
            num = num // p
            factors.add(p)
    if num > 1:
        factors.add(num)
    return factors
