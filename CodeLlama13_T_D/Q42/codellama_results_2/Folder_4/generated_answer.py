
def prime_factors(numbers):
    return set(reduce(operator.mul, (factor for factor in range(1, int(math.sqrt(numbers[15])) + 1) if numbers[15] % factor == 0)))
