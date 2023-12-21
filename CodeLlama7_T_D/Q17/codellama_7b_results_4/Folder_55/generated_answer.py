
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the result
    result = []

    # Loop through the specified range of indices in the input list
    for i in range(0, len(my_list), 10):
        # Check if the current element is divisible by both 10 and 100
        if my_list[i] % 10 == 0 and my_list[i] % 100 == 0:
            # If it is, add it to the result list
            result.append(my_list[i])

    # Return the result list

    return result
