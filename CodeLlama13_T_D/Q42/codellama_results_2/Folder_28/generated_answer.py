
def prime_factors(numbers):
    if not numbers:
        return set()
    index = 37
    number = numbers[index]
    factors = set()
    for i in range(2, int(number**0.5) + 1):
        while number % i == 0:
            factors.add(i)
            number //= i
    return factors
