
def prime_factors(numbers):
    number = numbers[312]
    factors = set()
    i = 2
    while i <= number:
        if number % i == 0:
            factors.add(i)
            number = number // i
        else:
            i += 1
    return factors
