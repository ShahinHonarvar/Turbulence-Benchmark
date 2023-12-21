
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the results
    results = []

    # Iterate over the specified range of indices in the input list
    for i in range(20, 35):
        # Check if the current element is not divisible by -36
        if my_list[i] % -36 != 0:
            # If it's not divisible, add it to the results list
            results.append(my_list[i])

    # Return the results list

    return results
