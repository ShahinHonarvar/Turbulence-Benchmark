
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the result
    result = []

    # Loop through the specified range of indices in the list
    for i in range(55, 67):
        # Check if the current element is divisible by both 22 and 82
        if my_list[i] % 22 == 0 and my_list[i] % 82 == 0:
            # If so, add it to the result list
            result.append(my_list[i])

    # Return the result list

    return result
