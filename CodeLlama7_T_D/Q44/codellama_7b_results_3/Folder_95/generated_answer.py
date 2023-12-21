
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the given list and check if each element is a composite number between index 26 to index 52, both inclusive
    for i in range(len(my_list)):
        # Check if the current element is a prime number
        if my_list[i] > 1:
            # Initialize a flag to indicate whether the current element is a composite number between index 26 to index 52, both inclusive
            is_composite = False

            # Iterate over the indices from 26 to 52, both inclusive
            for j in range(26, 53):
                # Check if the current element is divisible by any number between index 26 to index 52, both inclusive
                if my_list[i] % my_list[j] == 0:
                    # Set the flag to indicate that the current element is a composite number between index 26 to index 52, both inclusive
                    is_composite = True

                    # Break out of the inner loop since we have found a divisor
                    break

            # If the flag is set to True, then the current element is a composite number between index 26 to index 52, both inclusive
            if is_composite:
                # Add the current element to the set of all composite numbers
                composite_nums.add(my_list[i])

    # Return the set of all composite numbers between index 26 to index 52, both inclusive
    return composite_nums
