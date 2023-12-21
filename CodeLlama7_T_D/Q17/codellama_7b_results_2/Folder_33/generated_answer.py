
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the results
    result = []

    # Loop through the specified range of the input list
    for i in range(281, 695):
        # Check if the current element is divisible by both -722 and -731
        if my_list[i] % -722 == 0 and my_list[i] % -731 == 0:
            # If it is, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
