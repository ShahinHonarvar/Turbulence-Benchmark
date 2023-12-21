
def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("The input must be a list of positive integers")
    # Define the range of indices to check
    min_index = 14
    max_index = 64
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate over the elements in the input list within the specified range
    for i in range(min_index, len(my_list)):
        # Check if the current element is a prime number
        if my_list[i] > 1:
            # Initialize a flag to indicate whether the current element is a composite number
            is_composite = False

            # Iterate over the factors of the current element within the specified range
            for j in range(min_index, len(my_list)):
                # Check if the current element is divisible by the current factor
                if my_list[i] % my_list[j] == 0:
                    # If the current element is divisible by the current factor, set the flag to True and break out of the loop
                    is_composite = True
                    break

            # If the flag is False, add the current element to the set of composite numbers
            if not is_composite:
                composite_nums.add(my_list[i])

    # Return the set of composite numbers within the specified range
    return composite_nums
