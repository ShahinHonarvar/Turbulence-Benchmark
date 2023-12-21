
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the results
    result = []

    # Iterate over the elements of the tuple
    for i in range(len(tuple)):
        # Extract the current element from the tuple
        element = tuple[i]

        # Check if the current element is a prime number
        if is_prime(element):
            # Initialize an empty list to store the right-truncatable prime numbers less than the current element
            temp = []

            # Iterate over the digits of the current element
            for j in range(len(str(element)) - 1, -1, -1)):
                # Extract the current digit from the string representation of the current element
                digit = str(element)[j]

                # Check if the current digit is a prime number
                if is_prime(digit):
                    # Add the current element to the list of right-truncatable prime numbers
                    temp.append(element)

            # Sort the list of right-truncatable prime numbers in descending order
            temp.sort(reverse=True)

            # Add the sorted list of right-truncatable prime numbers to the result list
            result.extend(temp)

    return result
