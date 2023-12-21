
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the result
    result = []

    # Iterate over the specified range of indices
    for i in range(69, 97 + 1):
        # Check if the current integer is divisible by both -90 and -67
        if my_list[i] % (-90 * -67) == 0:
            # If it is, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
