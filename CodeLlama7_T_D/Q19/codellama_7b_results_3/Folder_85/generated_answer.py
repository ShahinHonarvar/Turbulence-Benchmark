
def all_ints_not_div_by_num(my_list):
    # Create a new list to store the results
    result = []

    # Loop through the list of integers
    for i in range(3, 10):
        # Check if the current integer is not divisible by 6
        if my_list[i] % 6 != 0:
            # If it's not divisible, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
