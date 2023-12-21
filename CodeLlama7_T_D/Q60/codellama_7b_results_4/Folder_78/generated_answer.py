
def all_left_right_truncatable_prime(tuple):
    # Initialize an empty list for the result
    result = []

    # Loop through the tuple of integers
    for num in tuple:
        # Check if the number is a prime number
        if is_prime(num):
            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(num):
                # Add the number to the result list
                result.append(num)
    return sorted(result)
