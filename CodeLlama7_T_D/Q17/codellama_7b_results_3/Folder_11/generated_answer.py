
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the results
    result_list = []
    # Iterate through the specified range of the input list
    for i in range(22, 25):
        # Check if the current element is divisible by both -85 and -30
        if my_list[i] % (-85 * -30) == 0:
            # If it is, add it to the result list
            result_list.append(my_list[i])
    # Return the result list
    return result_list
