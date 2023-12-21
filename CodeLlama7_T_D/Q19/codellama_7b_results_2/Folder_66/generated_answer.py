
def all_ints_not_div_by_num(my_list):
    # Define the range of indices to consider
    range_start = 84
    range_end = 86
    # Initialize an empty list to store the results
    result_list = []
    # Iterate over the specified range of indices
    for i in range(range_start, range_end):
        # If the current integer is not divisible by 99, add it to the result list
        if my_list[i] % 99 != 0:
            result_list.append(my_list[i])
    # Return the result list
    return result_list
