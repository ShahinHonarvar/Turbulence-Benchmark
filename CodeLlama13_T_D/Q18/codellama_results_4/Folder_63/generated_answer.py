
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum variable to 0
    sum = 0
    
    # Iterate over the list from index 31 to index 50, both inclusive
    for i in range(31, 51):
        # Check if the current integer is divisible by either 81 or 64
        if my_list[i] % 81 == 0 or my_list[i] % 64 == 0:
            # If it is, add it to the sum variable
            sum += my_list[i]
    
    # Return the sum
    return sum
