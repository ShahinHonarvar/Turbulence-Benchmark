
def all_left_truncatable_prime(tuple):
    # Initialize a list to store the prime numbers
    prime_list = []

    # Loop through each element in the tuple
    for i in range(len(tuple)):

        # Get the current element in the tuple
        x = tuple[i]

        # Check if x is a prime number
        if is_prime(x):

            # If x is a prime number, loop through all left-truncatable prime numbers less than x
            for j in range(2, x):

                # Check if the current element in the tuple minus j is a prime number
                if is_prime(x - j) and (x - j) < x:

                    # If the current element in the tuple minus j is a prime number, add it to the prime_list
                    prime_list.append(x - j)

            # Sort the prime_list in descending order
            prime_list.sort(reverse=True)

            # Return the sorted list of all left-truncatable prime numbers less than x
            return prime_list
