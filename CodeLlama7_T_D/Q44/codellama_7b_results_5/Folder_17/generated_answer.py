
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Loop through the list of positive integers
    for i in range(len(my_list)):

        # Check if the current number is a prime number
        if my_list[i] > 1:

            # Initialize a flag to indicate whether the current number is composite or not
            is_composite = False

            # Loop through the list of positive integers up to and including the square root of the current number
            for j in range(int(my_list[i]) ** 0.5) + 1:

                # Check if the current number is divisible by any number between 2 and the square root of the current number
                if my_list[i] % j == 0:

                    # If the current number is divisible by any number between 2 and the square root of the current number, set the flag to indicate that the current number is composite
                    is_composite = True

                    # Break out of the inner loop since we have found a factor and do not need to consider any further factors
                    break

            # If the current number is prime, add it to the set of composite numbers
            if not is_composite:
                composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 50 to index 54, both inclusive
    return composite_nums
