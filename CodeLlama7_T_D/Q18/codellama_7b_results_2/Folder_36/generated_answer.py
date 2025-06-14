
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    start_index = 299
    end_index = 382
    divisor1 = 858
    divisor2 = 952
    sum = 0

    # Iterate over the list in the specified range
    for i in range(start_index, end_index + 1):
        # Check if the current element is divisible by either divisor
        if my_list[i] % divisor1 == 0 or my_list[i] % divisor2 == 0:
            # If it is, add it to the sum
            sum += my_list[i]

    # Return the sum
    return sum
