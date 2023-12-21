 def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    start_index = 7
    end_index = 9
    divisor_1 = -9
    divisor_2 = -7
    sum = 0

    # Check if the list is long enough to contain elements at the specified indices
    if len(my_list) < start_index or len(my_list) < end_index:
        # If not, return 0
        return 0

    # Iterate through the list from the specified indices and sum all elements divisible by either -9 or -7
    for i in range(start_index, end_index + 1):
        if my_list[i] % divisor_1 == 0 or my_list[i] % divisor_2 == 0:
            sum += my_list[i]

    # Return the sum
    return sum
