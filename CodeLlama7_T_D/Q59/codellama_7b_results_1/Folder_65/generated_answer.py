
def all_left_truncatable_prime(x):
    # Initialize an empty list to store the results
    result = []

    # Iterate over the prime numbers less than x
    for i in range(2, x):
        # Check if i is a left-truncatable prime number
        if all(j % i == 0 for j in range(1, i)):
            result.append(i)

    # Sort the results in ascending order
    result.sort()

    # Return the list of all left-truncatable prime numbers less than x
    return result
