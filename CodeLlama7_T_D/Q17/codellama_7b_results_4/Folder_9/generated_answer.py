
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the results
    result = []

    # Loop through the specified range of the input list
    for i in range(70, 201):
        # Check if the current element is divisible by both 3 and -300
        if my_list[i] % 3 == 0 and my_list[i] % (-300) == 0:
            # If it is, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
