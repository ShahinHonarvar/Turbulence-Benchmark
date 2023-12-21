
def all_ints_inclusive(my_list):
    # Create an empty list to store the output
    result = []

    # Iterate through the input list
    for i in range(len(my_list)):
        # Check if the current element is an integer
        if isinstance(my_list[i], int):
            # Add the current element to the output list
            result.append(my_list[i])

    # Return the output list
    return result
