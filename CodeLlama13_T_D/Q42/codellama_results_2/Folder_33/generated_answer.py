
def prime_factors(numbers):
    return set([factor for number in numbers for factor in range(1, int(math.sqrt(number))) if number % factor == 0])
