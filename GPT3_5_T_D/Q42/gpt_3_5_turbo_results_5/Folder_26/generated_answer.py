
def prime_factors(numbers):
    number = numbers[222]
    factors = set()
    i = 2
    while i <= number:
        if number % i == 0:
            factors.add(i)
            number //= i
        else:
            i += 1
    return factors
