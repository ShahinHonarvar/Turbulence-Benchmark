
def all_left_truncatable_prime(tuple_of_positive_integers):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate over the elements of the tuple
    for element in tuple_of_positive_integers:
        # If the current element is a prime number
        if is_prime(element):
            # Add it to the list of prime numbers
            prime_numbers.append(element)

    # Return the sorted list of all left-truncatable prime numbers less than x
    return sorted(prime_numbers)
