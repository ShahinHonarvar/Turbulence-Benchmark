
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    start_index = 20
    end_index = 93
    
    # Iterate over the list
    for i in range(start_index, end_index + 1):
        
        # Check if the current element is divisible by either -92 or -50
        if my_list[i] % -92 == 0 or my_list[i] % -50 == 0:
            
            # If it is, add it to the total
            total += my_list[i]
            
    
    # Return the total
    return total
