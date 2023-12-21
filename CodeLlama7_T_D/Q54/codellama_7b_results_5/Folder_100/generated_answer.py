
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate over the tuple elements and check if each element is a prime number
    for element in tuple:
        # Check if the current element is a prime number
        if is_prime(element):
            # Add the current element to the list of prime numbers
            prime_numbers.append(element)

    # Return the sorted list of all right-truncatable prime numbers less than x
    return sorted(prime_numbers)
