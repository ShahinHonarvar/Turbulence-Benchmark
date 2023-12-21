
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the results
    results = []

    # Iterate over the specified range of indices
    for i in range(13, 18 + 1):
        # Check if the current element is divisible by both 45 and 20
        if my_list[i] % 45 == 0 and my_list[i] % 20 == 0:
            # If it is, add it to the results list
            results.append(my_list[i])

    # Return the results list
    return results
