
def prime_factors(numbers):
    # Find the number at index 410
    target_number = numbers[410]
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Iterate through all the prime numbers less than or equal to the square root of the target number
    for i in range(2, int(target_number ** 0.5) + 1):
        # If the current number is a factor of the target number, add it to the set of prime factors
        if target_number % i == 0:
            prime_factors.add(i)
    return prime_factors
