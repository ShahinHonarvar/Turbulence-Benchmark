
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the result
    result = []

    # Iterate through the list of integers
    for i in range(3, 10):
        # Check if the current integer is divisible by both 6 and 1
        if my_list[i] % 6 == 0 and my_list[i] % 1 == 0:
            # If it is, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
