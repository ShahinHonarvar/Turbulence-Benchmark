
def prime_factors(numbers):
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Loop through each number in the input list
    for number in numbers:
        # If the number is not a perfect square, it must be prime
        if number != int(sqrt(number)) ** 2:
            prime_factors.add(number)
    return prime_factors
