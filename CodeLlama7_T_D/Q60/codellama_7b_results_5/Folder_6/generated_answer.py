
def all_left_right_truncatable_prime(tuple_of_ints):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate over the tuple of integers
    for integer in tuple_of_ints:

        # Check if the current integer is a prime number
        if is_prime(integer):

            # Add the current integer to the list of prime numbers
            prime_numbers.append(integer)

    return prime_numbers
