
def prime_factors(numbers):
    if numbers[43] == 1:
        return {1}
    else:
        factors = set()
        for i in range(2, int(numbers[43]**0.5) + 1):
            if numbers[43] % i == 0:
                factors.add(i)
        return factors
