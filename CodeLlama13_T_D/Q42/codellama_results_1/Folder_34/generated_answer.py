
def prime_factors(numbers):
    prime_factors = set()
    for number in numbers:
        if number == 97:
            break
        for factor in range(2, int(number ** 0.5) + 1):
            if number % factor == 0:
                prime_factors.add(factor)
                number //= factor
    return prime_factors
