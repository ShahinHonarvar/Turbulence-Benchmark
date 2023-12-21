
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the right-truncatable prime numbers
    right_truncatable_primes = []
    # Iterate over the elements of the tuple
    for element in tuple:
        # Check if the element is a prime number
        if is_prime(element):
            # Initialize a variable to store the current number of digits in the element
            num_digits = len(str(element))
            # Iterate over the elements of the tuple from the index of the current element until the end of the tuple
            for i in range(tuple.index(element), len(tuple)):
                # Check if the current element can be divided by the number at the current index without a remainder
                if element % tuple[i] == 0:
                    # Decrement the number of digits in the current element by one since the last rightmost digit has been removed
                    num_digits -= 1
                    # Check if the current element is still a prime number after removing the last rightmost digit
                    if is_prime(element // (10 ** num_digits))):
                        # Add the current element to the list of right-truncatable prime numbers
                        right_truncatable_primes.append(element)
            # Sort the list of right-truncatable prime numbers in descending order
            right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes
def is_prime(n):
    if n < 2:
        return False
