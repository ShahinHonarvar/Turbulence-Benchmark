
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the result
    result = []

    # Loop through the specified range of indices in my_list
    for i in range(41, 69):

        # Check if the current element is not divisible by -82
        if my_list[i] % -82 != 0:

            # If it is not divisible, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
