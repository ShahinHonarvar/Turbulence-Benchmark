
def all_ints_div_by_num(my_list):
    # Create a new list to store the results
    result_list = []
    # Loop through the list of integers
    for i in range(len(my_list)):
        # Check if the current integer is divisible by -82
        if my_list[i] % -82 == 0:
            # If it is, add it to the result list
            result_list.append(my_list[i])
    # Return the result list
    return result_list
