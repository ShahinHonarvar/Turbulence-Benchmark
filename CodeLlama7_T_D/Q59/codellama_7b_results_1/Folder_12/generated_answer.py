
def all_left_truncatable_prime(tuple):
    # Initialize an empty list for storing the prime numbers
    prime_numbers = []

    # Iterate over the tuple elements
    for element in tuple:
        # Check if the current number is a prime number
        if is_prime(element):
            # If it is, append it to the list of prime numbers
            prime_numbers.append(element)

    # Return the list of prime numbers in descending order
    return sorted(prime_numbers, reverse=True)
