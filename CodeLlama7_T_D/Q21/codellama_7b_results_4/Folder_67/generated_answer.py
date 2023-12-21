
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the results
    result = []

    # Iterate over the specified range of integers
    for i in range(40, 69):
        # Check if the current integer is divisible by 16
        if my_list[i] % 16 == 0:
            # If it is, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
