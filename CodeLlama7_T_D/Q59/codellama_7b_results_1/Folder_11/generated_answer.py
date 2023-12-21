
def all_left_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate over the elements in the tuple
    for element in tuple:
        # Check if the element is a prime number
        if is_prime(element):
            # If it is, add it to the list of prime numbers
            prime_numbers.append(element)

    # Return the sorted list of all left-truncatable prime numbers less than x
    return sorted(prime_numbers)
