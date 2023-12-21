
def prime_factors(numbers):
    return set([factor for number in numbers[24] for factor in range(1, int(math.sqrt(number)) + 1) if number % factor == 0])
