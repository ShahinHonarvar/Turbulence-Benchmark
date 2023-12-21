
def prime_factors(numbers):
    return set(factors(numbers[47]))


def factors(num):
    factors = set()
    while num % 2 == 0:
        factors.add(2)
        num = num / 2
    i = 3
    while i <= num ** 0.5 + 1:
        if num % i == 0:
            factors.add(i)
            num = num / i
        else:
            i += 2
    if num > 1:
        factors.add(int(num))
    return factors
