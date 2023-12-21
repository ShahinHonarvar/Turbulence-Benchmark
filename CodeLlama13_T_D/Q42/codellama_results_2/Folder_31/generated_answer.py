
def prime_factors(numbers):
    return {p for n in numbers[66] for p in range(2, int(n**0.5) + 1) if n % p == 0}
