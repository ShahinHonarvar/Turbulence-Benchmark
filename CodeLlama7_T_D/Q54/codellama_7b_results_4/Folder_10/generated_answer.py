
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate over the elements in the tuple
    for element in tuple:
        # Check if the current element is a prime number
        if is_prime(element):
            # If it is, append it to the list of prime numbers
            prime_numbers.append(element)

    # Return the sorted list of right-truncatable prime numbers less than x
    return sorted(prime_numbers, key=lambda x: -x)
