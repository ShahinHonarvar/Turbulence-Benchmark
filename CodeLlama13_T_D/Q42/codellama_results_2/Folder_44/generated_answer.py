
def prime_factors(numbers):
    return set([factor for number in numbers[828] for factor in range(1, int(number**0.5) + 1) if number % factor == 0 and isprime(factor)])
