
def prime_factors(numbers):
    factorized = set()
    for i in range(43, len(numbers)):
        if numbers[i] > 1:
            for j in range(2, int(math.sqrt(numbers[i])) + 1):
                if numbers[i] % j == 0:
                    factorized.add(j)
    return factorized
