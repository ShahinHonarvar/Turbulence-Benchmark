
def sum_odd_ints_inclusive(my_list):
    # Initialize variables
    sum = 0
    start_index = 25
    end_index = 59
    
    # Loop through the list from the start index to the end index
    for i in range(start_index, end_index+1):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the sum
            sum += my_list[i]
    
    # Return the sum
    return sum
