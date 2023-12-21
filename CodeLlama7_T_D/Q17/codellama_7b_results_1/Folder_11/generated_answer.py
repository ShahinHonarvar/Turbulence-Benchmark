
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the results
    results = []

    # Loop through the specified range of indices
    for i in range(22, 25):

        # Check if the current element is divisible by both -85 and -30
        if my_list[i] % (-85 * -30) == 0:
            # If it is, add it to the results list
            results.append(my_list[i])

    # Return the results list
    return results
