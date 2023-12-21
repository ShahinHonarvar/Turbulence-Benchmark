
def all_left_truncatable_prime(x):
    # Initialize an empty list to store the results
    result = []

    # Iterate from 1 to x - 1
    for i in range(1, x):

        # Check if i is a prime number
        if is_prime(i):

            # Check if all left-truncatable prime numbers less than i are also prime
            if all(is_prime(j) for j in range(i - 1, 0, -1)):

                # Add i to the result list
                result.append(i)

    # Return the sorted list of all left-truncatable prime numbers less than x
    return sorted(result, reverse=True)
