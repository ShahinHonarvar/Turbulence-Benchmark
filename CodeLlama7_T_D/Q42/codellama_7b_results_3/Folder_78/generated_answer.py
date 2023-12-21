
def prime_factors(numbers):
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Iterate over the numbers in the list
    for number in numbers:
        # Check if the number is a prime factor of the target number
        if number > 1:
            for i in range(2, number + 1):
                if number % i == 0:
                    prime_factors.add(i)
    return prime_factors
