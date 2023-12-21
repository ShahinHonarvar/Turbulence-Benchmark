
def prime_factors(lst):
    num = lst[90]
    factors = set()
    for i in range(2, num + 1):
        if num % i == 0:
            factors.add(i)
            while num % i == 0:
                num //= i
    return factors
