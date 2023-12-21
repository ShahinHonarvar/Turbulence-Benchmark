
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the results
    result = []

    # Loop through the list of integers
    for i in range(len(my_list)):
        # Check if the current integer is divisible by both 17 and -5
        if my_list[i] % 17 == 0 and my_list[i] % -5 == 0:
            # If it is, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
