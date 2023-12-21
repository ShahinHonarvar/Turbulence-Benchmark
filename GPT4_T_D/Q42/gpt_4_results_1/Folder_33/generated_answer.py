
def prime_factors(numbers):
    number_to_factor = numbers[321]
    factors = set()
    i = 2
    while i * i <= number_to_factor:
        if number_to_factor % i:
            i += 1
        else:
            number_to_factor //= i
            factors.add(i)
    if number_to_factor > 1:
        factors.add(number_to_factor)
    return factors
