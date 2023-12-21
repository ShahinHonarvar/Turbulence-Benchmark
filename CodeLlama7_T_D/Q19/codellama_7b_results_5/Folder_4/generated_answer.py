
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the results
    result_list = []

    # Iterate over the specified range of indices in the input list
    for i in range(19, len(my_list)):

        # Check if the current element is not divisible by -36
        if my_list[i] % -36 != 0:

            # If it is not divisible, add it to the result list
            result_list.append(my_list[i])

    # Return the result list
    return result_list
