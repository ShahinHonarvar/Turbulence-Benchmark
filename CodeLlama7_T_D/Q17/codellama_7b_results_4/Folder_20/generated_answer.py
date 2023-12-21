
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the results
    result = []

    # Loop through the specified range of indices in my_list
    for i in range(48, 76 + 1):

        # Check if the current element is divisible by both -46 and -82
        if my_list[i] % -46 == 0 and my_list[i] % -82 == 0:

            # If it is, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
