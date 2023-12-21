
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables to keep track of the sum and the current index
    sum = 0
    i = 50
    # Loop through the list, starting from index 50
    while i < 93:
        # Check if the current element is divisible by either -94 or -95
        if my_list[i] % -94 == 0 or my_list[i] % -95 == 0:
            # If it is, add it to the sum
            sum += my_list[i]
        # Increment the current index by 1
        i += 1
    # Return the sum
    return sum
