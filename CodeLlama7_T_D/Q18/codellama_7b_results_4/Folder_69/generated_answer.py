
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    start_index = 61
    end_index = 88
    sum = 0

    # Iterate through the list
    for i in range(start_index, end_index + 1):
        # Check if the current index is divisible by either num
        if my_list[i] % 31 == 0 or my_list[i] % 11 == 0:
            # Add the current element to the sum
            sum += my_list[i]

    # Return the sum
    return sum
