
def prime_factors(numbers):
    return set([n for n in range(2, max(numbers) + 1) if all(number % n == 0 for number in numbers)])
