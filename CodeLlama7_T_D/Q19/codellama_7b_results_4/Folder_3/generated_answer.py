
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the results
    result = []

    # Iterate over the list of integers
    for i in range(31, 69):
        # Check if the current integer is not divisible by -70
        if my_list[i] % -70 != 0:
            # If it is not divisible, add it to the results list
            result.append(my_list[i])

    # Return the results list
    return result
