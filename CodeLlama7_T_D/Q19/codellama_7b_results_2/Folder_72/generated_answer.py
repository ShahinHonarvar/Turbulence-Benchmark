
def all_ints_not_div_by_num(my_list):
    # Find the first index of -78 in the list
    start_index = my_list.index(-78)
    # Find the last index of -78 in the list
    end_index = my_list[::-1].index(-78)
    # Initialize an empty list to store the result
    result = []
    # Iterate through the list and check if each integer is not divisible by -78
    for i in range(start_index, end_index):
        if my_list[i] % -78 != 0:
            result.append(my_list[i])
    # Return the result list
    return result
