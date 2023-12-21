
def prime_factors(numbers):
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Iterate over the numbers in the list
    for number in numbers:
        # Check if the number is a prime factor of the current number
        if number > 1 and all(number % i != 0 for i in range(2, number))):
            # Add the prime factor to the set
            prime_factors.add(number)
    return prime_factors
