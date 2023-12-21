
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the results
    result = []

    # Iterate over the specified range of the input list
    for i in range(24, 32 + 1):
        # Check if the current element is divisible by both 35 and 87
        if my_list[i] % 35 == 0 and my_list[i] % 87 == 0:
            # If it is, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
