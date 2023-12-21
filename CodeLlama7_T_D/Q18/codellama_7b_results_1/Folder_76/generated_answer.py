
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    sum = 0
    # Loop through the list from index 250 to index 629, both inclusive
    for i in range(250, 630):
        # Check if the current element is divisible by either 850 or 587
        if my_list[i] % 850 == 0 or my_list[i] % 587 == 0:
            # If it is, add it to the sum
            sum += my_list[i]
    # Return the sum
    return sum
