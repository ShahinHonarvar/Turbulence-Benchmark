
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    start_index = 154
    end_index = 798
    sum = 0

    # Iterate through the list from the start index to the end index
    for i in range(start_index, end_index + 1):
        # Check if the current element is divisible by either 275 or 580
        if my_list[i] % 275 == 0 or my_list[i] % 580 == 0:
            # If it is, add it to the sum
            sum += my_list[i]

    # Return the sum
    return sum
