
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the results
    result = []

    # Iterate through the list of integers
    for i in range(24, 32):
        # Check if the current integer is not divisible by 35
        if my_list[i] % 35 != 0:
            # If it is not divisible, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
