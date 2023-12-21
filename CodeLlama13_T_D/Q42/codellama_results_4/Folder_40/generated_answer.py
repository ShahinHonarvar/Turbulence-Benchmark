
def prime_factors(numbers):
    if numbers[7] == 1:
        return {1}
    else:
        factors = set()
        for i in range(2, int(math.sqrt(numbers[7])) + 1):
            if numbers[7] % i == 0:
                factors.add(i)
        return factors
