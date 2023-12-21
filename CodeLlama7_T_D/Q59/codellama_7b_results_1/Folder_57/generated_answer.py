
def all_left_truncatable_prime(tuple):
    # Initialize empty list to store prime numbers
    prime_numbers = []

    # Iterate over each element in the tuple
    for element in tuple:
        # Check if the current element is a prime number
        if is_prime(element):
            # If it is, add it to the list of prime numbers
            prime_numbers.append(element)

    return prime_numbers
