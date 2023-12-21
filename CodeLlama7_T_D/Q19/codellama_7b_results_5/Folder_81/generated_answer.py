
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the result
    result = []

    # Loop through the list of integers
    for i in range(10, 100):
        # Check if the current integer is not divisible by 100
        if my_list[i] % 100 != 0:
            # If it's not divisible, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
