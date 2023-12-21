
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the results
    result_list = []

    # Iterate through the list of integers
    for i in range(39, 57):
        # Check if the current integer is not divisible by 84
        if my_list[i] % 84 != 0:
            # If it is not divisible, add it to the result list
            result_list.append(my_list[i])

    # Return the result list
    return result_list
