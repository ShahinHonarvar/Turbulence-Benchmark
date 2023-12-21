
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the results
    result = []

    # Iterate over the specified range of indices
    for i in range(44, 60):
        # Check if the current integer is divisible by both 39 and 15
        if my_list[i] % 39 == 0 and my_list[i] % 15 == 0:
            # If it is, add it to the results list
            result.append(my_list[i])

    # Return the results list
    return result
