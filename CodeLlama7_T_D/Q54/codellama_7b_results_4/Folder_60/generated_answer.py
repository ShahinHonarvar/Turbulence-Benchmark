
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the right-truncatable prime numbers
    right_truncatable_primes = []

    # Iterate over each element in the tuple
    for element in tuple:

        # Check if the current element is a prime number
        if is_prime(element):

            # Initialize a variable to store the current element as a string
            current_element_as_string = str(element)

            # Iterate over each character in the current element as a string
            for character in current_element_as_string:

                # Check if removing the last rightmost digit from the current element results in a prime number
                if is_prime(int(current_element_as_string[:-1])):

                    # Add the current element to the list of right-truncatable prime numbers
                    right_truncatable_primes.append(element)

            # Sort the list of right-truncatable prime numbers in ascending order
            sorted_right_truncatable_primes = sorted(right_truncatable_primes)

            # Return the sorted list of right-truncatable prime numbers
            return sorted_right_truncatable_primes

        else:

            # If the current element is not a prime number, return an empty list
            return []
