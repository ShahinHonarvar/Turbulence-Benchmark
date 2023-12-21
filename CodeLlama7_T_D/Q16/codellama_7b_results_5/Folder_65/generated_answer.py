
def sum_even_ints_inclusive(my_list):
    # Initialize variables
    total = 0
    start_index = 56
    end_index = 98
    
    # Iterate through the list and add up the even integers
    for i in range(start_index, end_index + 1):
        if my_list[i] % 2 == 0:
            total += my_list[i]
            
    # Return the sum of all even integers in the specified range
    return total
