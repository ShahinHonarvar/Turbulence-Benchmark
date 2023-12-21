
def sum_ints_div_by_either_nums(my_list):
    # Initialize a variable to store the sum
    sum = 0
    
    # Iterate over the list from index 81 to 89, both inclusive
    for i in range(81, 90):
        # Check if the current element is divisible by either 56 or 68
        if my_list[i] % 56 == 0 or my_list[i] % 68 == 0:
            # If it is, add it to the sum
            sum += my_list[i]
    
    # Return the sum
    return sum
