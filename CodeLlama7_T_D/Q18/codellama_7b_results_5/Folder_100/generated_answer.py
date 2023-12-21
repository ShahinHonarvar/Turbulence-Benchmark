
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables to keep track of the sum and the current index in the list
    total = 0
    current_index = 72
    # Loop through the list from the specified starting index to the end of the list
    while current_index < len(my_list):
        # Check if the current element is divisible by either 32 or 44
        if my_list[current_index] % 32 == 0 or my_list[current_index] % 44 == 0:
            # If it is, add it to the total sum
            total += my_list[current_index]
        # Increment the current index by 1
        current_index += 1
    # Return the total sum
    return total
