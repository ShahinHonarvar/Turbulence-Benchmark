
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables for the desired range and the sum of divisible integers
    start_index = 828
    end_index = 932
    total_sum = 0

    # Iterate through the list in the specified range
    for i in range(start_index, end_index + 1):
        # Check if the current integer is divisible by either -649 or -461
        if my_list[i] % (-649) == 0 or my_list[i] % (-461) == 0:
            # If it is, add it to the total sum
            total_sum += my_list[i]

    # Return the total sum of all divisible integers in the specified range
    return total_sum
