
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the results
    result_list = []
    # Iterate through the list of integers
    for i in range(10, 37 + 1):
        # Check if the current integer is divisible by -64
        if my_list[i] % -64 == 0:
            # If it is, add it to the result list
            result_list.append(my_list[i])
    # Return the result list
    return result_list
