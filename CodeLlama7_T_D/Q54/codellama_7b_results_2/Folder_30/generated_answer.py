
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through the tuple and check for each element if it is a prime number and if it is right-truncatable.
    for i in range(len(tuple)):
        x = tuple[i]
        if is_prime(x) and is_right_truncatable(x):
            # Add the prime number to the list of prime numbers
            prime_numbers.append(x)

    # Return the sorted list of all right-truncatable prime numbers less than x.
    return sorted(prime_numbers, reverse=True)
