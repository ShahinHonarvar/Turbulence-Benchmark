
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the result
    result = []

    # Loop through the specified range of indices in the input list
    for i in range(86, 91):
        # Check if the current integer is divisible by both -71 and -67
        if my_list[i] % -71 == 0 and my_list[i] % -67 == 0:
            # If it is, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
