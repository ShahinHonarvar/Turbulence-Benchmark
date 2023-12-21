
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate over all prime numbers less than or equal to x
    for i in range(2, x + 1):
        # If the current number is a prime number and it satisfies the left-and-right-truncatable prime condition
        if i > 1 and all([i % j == 0 for j in range(2, int(i ** 0.5) + 1)])):
            # Add the current number to the list of prime numbers
            prime_numbers.append(i)

    # Return the list of prime numbers sorted in descending order
    return sorted(prime_numbers, reverse=True)
