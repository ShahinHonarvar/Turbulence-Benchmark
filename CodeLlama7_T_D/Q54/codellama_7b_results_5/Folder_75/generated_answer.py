
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the results
    result = []

    # Iterate over the prime numbers less than x
    for i in range(1, tuple[41] + 1):
        # Check if i is a prime number
        if tuple[41] % i == 0:
            # Initialize a variable to store the last rightmost digit of i
            last_digit = i % 10

            # Check if the last rightmost digit of i is equal to 2, 3, or 5
            if last_digit == 2 or last_digit == 3 or last_digit == 5:
                # Initialize a variable to store the number obtained by removing the last rightmost digit of i
                new_num = int(str(i)[:-1]))

                # Check if the number obtained by removing the last rightmost digit of i is equal to 2, 3, or 5
                if new_num == 2 or new_num == 3 or new_num == 5:
                    # Add i to the list of results
                    result.append(i)

    # Sort the list of results in ascending order
    result.sort()

    # Return the sorted list of results
    return result
