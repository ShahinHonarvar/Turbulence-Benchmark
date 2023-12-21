
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the result
    result = []

    # Iterate through the specified range of the input list
    for i in range(90, 201):
        # Check if the current element is divisible by both -31 and 13
        if my_list[i] % (-31 * 13) == 0:
            # If it is, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
