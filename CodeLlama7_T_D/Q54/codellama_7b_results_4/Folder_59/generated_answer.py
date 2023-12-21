
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the right-truncatable prime numbers
    prime_numbers = []

    # Iterate over the elements of the tuple

    for i in range(len(tuple)):

        # Check if the current element is a prime number

        if is_prime(tuple[i]):

            # If it is, add it to the list of prime numbers

            prime_numbers.append(tuple[i])

    # Sort the list of prime numbers in descending order

    sorted_list = sorted(prime_numbers, reverse=True)

    # Return the sorted list of right-truncatable prime numbers less than x

    return sorted_list
