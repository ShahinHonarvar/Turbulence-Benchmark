
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the result
    result = []

    # Loop through the specified range of indices in my_list
    for i in range(55, 85):

        # Check if the current element is divisible by both -24 and -11
        if my_list[i] % (-24) == 0 and my_list[i] % (-11) == 0:

            # If it is, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
