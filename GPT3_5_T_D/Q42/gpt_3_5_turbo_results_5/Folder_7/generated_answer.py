
def prime_factors(numbers):
    number = numbers[851]
    factors = set()
    i = 2
    while i*i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            factors.add(i)
    if number > 1:
        factors.add(number)
    return factors
