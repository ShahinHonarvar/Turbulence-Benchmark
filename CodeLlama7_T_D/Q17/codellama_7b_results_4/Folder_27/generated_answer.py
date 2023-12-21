
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the result
    result = []

    # Iterate through the list of integers starting from index 20 to index 35, both inclusive
    for i in range(20, 36):
        # Check if the current integer is divisible by -36 and -89
        if my_list[i] % (-36 * -89) == 0:
            # If it is, add it to the result list
            result.append(my_list[i])

    # Return the result list

    return result
