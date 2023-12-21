
def prime_factors(numbers):
    return {prime for number in numbers[990].factors() if prime(number) is True}
