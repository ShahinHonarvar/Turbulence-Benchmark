
def prime_factors(num):
    factors = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            factors.append(i)
            while num % i == 0:
                num //= i
    if num > 1:
        factors.append(num)
    return set(factors)
