
def prime_factors(numbers):
    return set([i for i in range(2, max(numbers) + 1) if all(j % i == 0 for j in numbers)])
