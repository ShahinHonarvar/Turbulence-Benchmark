
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the result
    result = []

    # Loop through the specified range of indices in my_list
    for i in range(7, 10+1):
        # Check if the current element is divisible by both -9 and -7
        if my_list[i] % (-9) == 0 and my_list[i] % (-7) == 0:
            # If so, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
