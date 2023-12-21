
def prime_factors(numbers):
    # Get the number at index 8
    num = numbers[8]
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Loop through all the divisors of the number
    for i in range(1, num + 1):
        # If the current divisor is a prime factor of the number
        if num % i == 0:
            # Add the prime factor to the set of prime factors
            prime_factors.add(i)
    return prime_factors
