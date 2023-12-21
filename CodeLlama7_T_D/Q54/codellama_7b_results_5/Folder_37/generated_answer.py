
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the results
    result = []

    for i in range(len(tuple)):
        # Check if the current number is a prime number
        if tuple[i] == 2 or tuple[i] % 2 != 0:
            # Initialize a variable to keep track of the number of digits that have been removed from the current number
            num_digits = 0

            while True:
                # Check if the current number is a prime number after removing its last rightmost digit
                if tuple[i] % pow(10, num_digits) == 0 or tuple[i] == 2:
                    # If the current number is not a prime number after removing its last rightmost digit, break out of the while loop
                    break

                # Remove the last rightmost digit from the current number
                tuple[i] = int(str(tuple[i])[:-1]))

                # Increment the number of digits that have been removed from the current number
                num_digits += 1

            # If the current number is a prime number after removing its last rightmost digit, add it to the result list
            if tuple[i] % pow(10, num_digits) == 0 or tuple[i] == 2:
                result.append(tuple[i])

    # Sort the result list in descending order
    result = sorted(result, reverse=True)

    return result
