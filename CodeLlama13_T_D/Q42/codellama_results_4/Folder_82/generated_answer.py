
def prime_factors(numbers):
    return set([factor for factor in range(2, numbers[83]) if numbers[83] % factor == 0 and all(numbers[i] % factor != 0 for i in range(len(numbers)) if i != 83)])
