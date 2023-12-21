
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the results
    result = []

    # Loop through the specified range of indices in the input list
    for i in range(1, len(my_list)):

        # Check if the current element is not divisible by 8
        if my_list[i] % 8 != 0:

            # If it is not divisible by 8, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
