
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    i = 0
    
    # Loop through the list until we reach the end
    while i < len(my_list):
        # Check if the current element is divisible by either 1 or -1
        if my_list[i] % 1 == 0 or my_list[i] % -1 == 0:
            # If it is, add it to the sum
            sum += my_list[i]
        
        # Increment the index by 1
        i += 1
    
    # Return the sum
    return sum
