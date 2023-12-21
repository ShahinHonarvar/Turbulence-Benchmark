
def prime_factors(numbers):
    number = numbers[60]
    factors = set()
    for i in range(2, number):
        while number % i == 0:
            factors.add(i)
            number //= i
    if number > 1:
        factors.add(number)
    return factors
