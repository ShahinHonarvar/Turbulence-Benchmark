 def all_ints_div_by_both_two_nums(my_list):
    # Initialize the result list
    result = []
    # Iterate over the specified range of indices
    for i in range(42, 87+1):
        # Check if the current integer is divisible by both -90 and -74
        if my_list[i] % -90 == 0 and my_list[i] % -74 == 0:
            # If so, add it to the result list
            result.append(my_list[i])
    # Return the result list
    return result
