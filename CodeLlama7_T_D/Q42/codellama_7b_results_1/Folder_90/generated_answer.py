
def prime_factors(numbers):
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Iterate over the numbers in the list
    for number in numbers:
        # If the number is not a multiple of any previous prime factor, it is a prime factor itself
        if all(number % prime_factor != 0 for prime_factor in prime_factors):
            prime_factors.add(number)
    return prime_factors
