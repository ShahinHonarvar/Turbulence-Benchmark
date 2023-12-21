
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    sum = 0
    # Loop through the list starting from index 18
    for i in range(18, len(my_list)):
        # If the current element is divisible by either 15 or 57
        if my_list[i] % 15 == 0 or my_list[i] % 57 == 0:
            # Add the current element to the sum
            sum += my_list[i]
    # Return the sum
    return sum
