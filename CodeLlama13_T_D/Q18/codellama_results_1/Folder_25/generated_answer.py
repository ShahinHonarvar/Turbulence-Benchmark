
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    total = 0
    
    # Iterate over the list from index 25 to index 80, both inclusive
    for i in range(25, 81):
        # Check if the current element is divisible by either -20 or -26
        if my_list[i] % -20 == 0 or my_list[i] % -26 == 0:
            # If it is, add it to the total
            total += my_list[i]
    
    # Return the sum
    return total
