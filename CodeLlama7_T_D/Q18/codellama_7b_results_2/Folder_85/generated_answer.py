
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables to keep track of the sum and the current index
    total = 0
    current_index = 1
    
    # Loop through the list from the specified range
    for i in range(current_index, len(my_list)):
        
        # If the current element is divisible by either -9 or -3, add it to the sum
        if my_list[i] % (-9) == 0 or my_list[i] % (-3) == 0:
            total += my_list[i]
            
    # Return the sum of all integers divisible by either -9 or -3 from index 1 to index 8, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return total
