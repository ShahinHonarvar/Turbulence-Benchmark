
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the result
    result = []

    # Iterate through the list of integers
    for i in range(14, 93 + 1):

        # Check if the current integer is divisible by both 71 and 81
        if my_list[i] % 71 == 0 and my_list[i] % 81 == 0:

            # If it is, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
