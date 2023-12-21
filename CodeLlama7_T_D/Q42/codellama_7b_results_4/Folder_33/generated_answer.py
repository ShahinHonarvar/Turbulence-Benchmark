
def prime_factors(numbers):
    # Find the number at index 321
    number = numbers[321]
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Loop through all divisors of the number
    for i in range(1, number + 1):
        # If the number is divisible by the current divisor, add it to the set of prime factors
        if number % i == 0:
            prime_factors.add(i)
    return prime_factors
