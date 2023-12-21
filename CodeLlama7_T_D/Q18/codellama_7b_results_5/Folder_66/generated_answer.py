
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum variable
    sum = 0

    # Loop through the list of integers
    for i in range(58, 82):
        # Check if the current integer is divisible by either 55 or 10
        if my_list[i] % 55 == 0 or my_list[i] % 10 == 0:
            # If it is, add it to the sum
            sum += my_list[i]

    # Return the sum
    return sum
