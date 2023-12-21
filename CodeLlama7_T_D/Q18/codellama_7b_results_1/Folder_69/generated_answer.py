
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    index = 61

    # Loop through the list until we reach the end
    while index < len(my_list):
        # Check if the current element is divisible by either 31 or 11
        if my_list[index] % 31 == 0 or my_list[index] % 11 == 0:
            # If it is, add it to the sum
            sum += my_list[index]

        # Increment the index by 1
        index += 1

    # Return the sum
    return sum
