
def prime_factors(numbers):
    return set([factor for num in numbers if isinstance(num, int) and num > 0 for factor in range(1, num + 1) if num % factor == 0])
