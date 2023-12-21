
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the results
    result = []

    # Loop through the specified range of indices in the input list
    for i in range(20, 35+1):
        # Check if the current element is divisible by both -36 and -89
        if my_list[i] % (-36 * -89) == 0:
            # If it is, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
