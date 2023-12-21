
def all_left_truncatable_prime(tuple):
    # Initialize the list of left-truncatable prime numbers
    ltprimes = []

    # Iterate over the tuple and check if each element is a left-truncatable prime number
    for i in range(len(tuple)):
        x = tuple[i]

        # Check if x is a prime number

        if is_prime(x):

            # Check if x is a left-truncatable prime number

            if is_left_truncatable_prime(x):

                # Add x to the list of left-truncatable prime numbers

                ltprimes.append(x)

    # Sort the list of left-truncatable prime numbers in ascending order

    ltprimes = sorted(ltprimes)

    return ltprimes
