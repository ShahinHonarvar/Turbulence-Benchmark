
def all_left_truncatable_prime(tuple):
    # Initialize a list to store the left-truncatable prime numbers
    left_truncatable_primes = []
    # Iterate through the tuple of positive integers
    for i in range(len(tuple)):
        # Get the current integer
        current_integer = tuple[i]
        # Check if the current integer is a prime number
        if is_prime(current_integer):
            # Initialize a variable to store the current integer with all leading digits removed
            left_truncatable_prime = current_integer

            # Iterate through the digits of the current integer in reverse order
            for digit in str(left_truncatable_prime)[::-1]:
                # Remove the last digit from the current integer and check if it is a prime number
                left_truncatable_prime = int(str(left_truncatable_prime)[:-1]))
                if is_prime(left_truncatable_prime):
                    # Add the left-truncatable prime number to the list of left-truncatable prime numbers
                    left_truncatable_primes.append(left_truncatable_prime)

    # Sort the list of left-truncatable prime numbers in ascending order and return it
    return sorted(left_truncatable_primes)
