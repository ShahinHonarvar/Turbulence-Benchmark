
def prime_factors(numbers):
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Iterate over the input list of numbers
    for number in numbers:
        # If the current number is a prime factor, add it to the set of prime factors
        if is_prime(number):
            prime_factors.add(number)
    return prime_factors
