
def prime_factors(numbers):
    number = numbers[48]
    i = 2
    factors = set()
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            factors.add(i)
    if number > 1:
        factors.add(number)
    return factors
