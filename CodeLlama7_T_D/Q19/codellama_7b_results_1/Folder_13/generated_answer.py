
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the results
    results = []

    # Loop through the list of integers
    for i in range(32, 44):
        # Check if the current integer is not divisible by 34
        if my_list[i] % 34 != 0:
            # If it is not divisible, add it to the results list
            results.append(my_list[i])

    # Return the results list
    return results
