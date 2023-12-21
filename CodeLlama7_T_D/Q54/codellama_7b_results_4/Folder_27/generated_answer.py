
def all_right_truncatable_prime(tuple_of_integers):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate over the tuple of integers
    for integer in tuple_of_integers:
        # Check if the integer is a prime number
        if is_prime(integer):
            # Add the prime number to the list of prime numbers
            prime_numbers.append(integer)

    # Return the sorted list of all right-truncatable prime numbers less than x, or an empty list if there are no such prime numbers
    return sorted(prime_numbers, reverse=True)
