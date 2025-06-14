
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the results
    result = []

    # Iterate over the list of integers
    for i in range(59, 93):
        # Check if the current integer is not divisible by -26
        if my_list[i] % -26 != 0:
            # If it's not divisible, add it to the results list
            result.append(my_list[i])

    # Return the results list
    return result
