
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    start_index = 34
    end_index = 69
    divisor1 = 19
    divisor2 = 32
    total_sum = 0

    # Iterate over the list, starting from the specified index and ending at the specified index
    for i in range(start_index, end_index + 1):
        # Check if the current element is divisible by either 19 or 32
        if my_list[i] % divisor1 == 0 or my_list[i] % divisor2 == 0:
            # If it is, add it to the total sum
            total_sum += my_list[i]

    # Return the total sum
    return total_sum
