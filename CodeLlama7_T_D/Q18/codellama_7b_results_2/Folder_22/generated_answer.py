
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 40
    end_index = 200
    # Iterate through the list in the specified range
    for i in range(start_index, end_index + 1):
        # Check if the current element is divisible by either 21 or 71
        if my_list[i] % 21 == 0 or my_list[i] % 71 == 0:
            # Add the current element to the sum
            sum += my_list[i]
    return sum
