
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the results
    result = []

    # Iterate through the list of integers
    for i in range(50, 92):
        # Check if the current integer is not divisible by 16
        if my_list[i] % 16 != 0:
            # If it's not divisible, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
