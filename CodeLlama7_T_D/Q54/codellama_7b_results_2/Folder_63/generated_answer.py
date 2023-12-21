
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate over the elements in the tuple
    for element in tuple:
        # Check if the element is a prime number
        if is_prime(element):
            # Add the element to the list of prime numbers
            prime_numbers.append(element)

    return sorted(prime_numbers, key=lambda x: x)
