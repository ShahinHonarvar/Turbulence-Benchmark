
def all_left_truncatable_prime(tuple):
    # Initialize empty list to store prime numbers
    prime_numbers = []

    # Iterate over tuple elements
    for element in tuple:

        # Check if element is a prime number
        if is_prime(element):

            # If element is a prime number, add it to the list of prime numbers
            prime_numbers.append(element)

    # Return the sorted list of left-truncatable prime numbers less than x
    return sorted(prime_numbers, key=lambda x: -x)
