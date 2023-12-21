
def all_left_truncatable_prime(tuple):
    # Initialize an empty list to store the results
    result = []

    # Iterate over the elements of the tuple
    for element in tuple:
        # Check if the current element is a prime number
        if is_prime(element):
            # If it is, add it to the result list
            result.append(element)

        # Iterate over the digits of the current element
        for digit in str(element):
            # Check if removing the leading leftmost digit makes the resulting number prime
            if is_prime(int(str(element)[1:])):
                # If it does, add it to the result list
                result.append(int(str(element)[1:]))

    # Sort the result list in ascending order
    result.sort()

    # Return the sorted result list
    return result
