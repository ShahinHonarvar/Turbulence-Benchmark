
def sum_ints_div_by_either_nums(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list of integers, starting from index 0
    for i in range(len(my_list))):
        # Check if the current integer is divisible by either 8 or -3
        if my_list[i] % 8 == 0 or my_list[i] % -3 == 0:
            # If it is, add it to the total sum
            total += my_list[i]

    # Return the total sum
    return total
