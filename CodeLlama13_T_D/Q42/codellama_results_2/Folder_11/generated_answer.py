
def prime_factors(numbers):
    if not numbers:
        return set()
    prime_factors = []
    for number in numbers:
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                prime_factors.append(i)
                number //= i
        if number > 1:
            prime_factors.append(number)
    return set(prime_factors)
