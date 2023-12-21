
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the results
    result = []

    # Iterate over the range of numbers from 1 to x
    for i in range(1, x + 1):

        # Check if the current number is a prime number
        if is_prime(i):

            # If the current number is a prime number, check if it is left-and-right-truncatable
            if is_left_right_truncatable(i):

                # If the current number is both a prime number and left-and-right-truncatable, add it to the result list
                result.append(i)

    # Sort the result list in descending order
    result.sort(reverse=True)

    # Return the result list
    return result
