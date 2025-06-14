
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the results
    result = []

    # Iterate through the specified range of indices in the input list
    for i in range(20, 200 + 1):
        # Check if the current element is divisible by both -20 and -200
        if my_list[i] % (-20) == 0 and my_list[i] % (-200) == 0:
            # If it is, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
