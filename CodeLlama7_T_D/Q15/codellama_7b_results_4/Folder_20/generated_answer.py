
def sum_odd_ints_inclusive(my_list):
    # Initialize variables
    sum = 0
    start_index = 56
    end_index = 66
    
    # Iterate over the list and add up the odd integers within the specified range
    for i in range(start_index, end_index + 1):
        if my_list[i] % 2 != 0:
            sum += my_list[i]
            
    # Return the sum of all odd integers within the specified range
    return sum
