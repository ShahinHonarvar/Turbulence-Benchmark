
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the results
    result_list = []
    # Iterate over the specified range of the input list
    for i in range(81, 90):
        # Check if the current element is divisible by both 56 and 68
        if my_list[i] % 56 == 0 and my_list[i] % 68 == 0:
            # If it is, add it to the result list
            result_list.append(my_list[i])
    # Return the result list
    return result_list
