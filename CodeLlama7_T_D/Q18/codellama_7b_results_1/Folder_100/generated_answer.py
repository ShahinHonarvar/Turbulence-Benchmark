
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables to keep track of the sum and the index
    sum = 0
    i = 72
    # Loop through the list until the end is reached
    while i < len(my_list):
        # Check if the current element is divisible by either 32 or 44
        if my_list[i] % 32 == 0 or my_list[i] % 44 == 0:
            # If it is, add it to the sum
            sum += my_list[i]
        # Increment the index by 1
        i += 1
    # Return the sum
    return sum
