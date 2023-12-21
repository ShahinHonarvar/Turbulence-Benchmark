
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the results
    result = []

    # Iterate through the list of integers
    for i in range(len(my_list)):
        # Check if the current integer is divisible by -12
        if my_list[i] % -12 == 0:
            # If it is, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
