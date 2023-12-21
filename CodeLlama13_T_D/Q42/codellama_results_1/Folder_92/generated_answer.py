
def prime_factors(numbers):
    return set([i for i in range(2, numbers[0]+1) if numbers[0] % i == 0])
