
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum variable to 0
    sum = 0
    
    # Iterate over the list from index 38 to 81, both inclusive
    for i in range(38, 82):
        # Check if the current element is divisible by -61 or -71
        if my_list[i] % -61 == 0 or my_list[i] % -71 == 0:
            # If it is, add it to the sum variable
            sum += my_list[i]
    
    # Return the sum
    return sum
