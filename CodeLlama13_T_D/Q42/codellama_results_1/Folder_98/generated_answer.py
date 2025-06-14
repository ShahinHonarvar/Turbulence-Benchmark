
def prime_factors(numbers):
    return set([prime for number in numbers[4:] for prime in range(2, int(number**0.5) + 1) if not number % prime])
