
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Iterate over the tuple of integers
    for i in range(len(tuple)):
        # Get the current integer from the tuple
        current_integer = tuple[i]

        # Check if the current integer is a prime number
        if is_prime(current_integer):
            # If the current integer is a prime number, add it to the list of prime numbers
            prime_list.append(current_integer)

    # Sort the list of prime numbers in ascending order
    prime_list.sort()

    # Return the sorted list of prime numbers
    return prime_list
