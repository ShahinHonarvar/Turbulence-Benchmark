
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables to keep track of the sum and the current index
    total = 0
    i = 0
    
    # Loop through the list until we reach the end
    while i < len(my_list):
        
        # Check if the current element is divisible by either 2 or 1 from index 0 to index 1, both inclusive
        if my_list[i] % 2 == 0 or my_list[i] % 1 == 0:
            
            # If it is, add it to the sum
            total += my_list[i]
        
        # Increment the current index by 1
        i += 1
    
    # Return the sum of all integers divisible by either 2 or 1 from index 0 to index 1, both inclusive
    return total
