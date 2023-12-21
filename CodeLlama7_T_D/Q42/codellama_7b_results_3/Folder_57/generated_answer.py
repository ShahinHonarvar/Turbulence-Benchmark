
def prime_factors(numbers):
    # Initialize an empty set to store the prime factors
    prime_factors = set()

    # Iterate over the input list of numbers
    for number in numbers:
        # Check if the current number is a prime factor
        if is_prime_factor(number, numbers):
            # Add the prime factor to the set
            prime_factors.add(number)

    return prime_factors
