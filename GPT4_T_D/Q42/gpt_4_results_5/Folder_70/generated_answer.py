
def prime_factors(numbers):
    number = numbers[845]
    factors = []
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            factors.append(i)
    if number > 1:
        factors.append(number)
    prime_set = set(factors)
    return prime_set
