
def all_left_truncatable_prime(tuple):
    # Initialize an empty list to store the results
    result = []

    # Iterate over the tuple elements
    for i in range(len(tuple)):

        # Get the current element and its length
        num = tuple[i]
        len_num = len(str(num))

        # Check if the current number is prime
        if is_prime(num):

            # Initialize a flag to indicate whether the current number is left-truncatable prime
            flag = True

            # Iterate over the digits of the current number
            for j in range(len_num - 1):

                # Get the current digit and remove it from the string representation of the number
                curr_digit = str(num)[j]
                num = int(str(num)[:j] + str(num)[j+1:]))

                # Check if the current number is prime
                if not is_prime(num):

                    # Set the flag to False and break out of the inner loop
                    flag = False
                    break

            # If the flag is still True, then the current number is a left-truncatable prime number
            if flag:

                # Add the current number to the result list
                result.append(num)

    # Return the sorted list of all left-truncatable prime numbers less than x
    return sorted(result, reverse=True)
