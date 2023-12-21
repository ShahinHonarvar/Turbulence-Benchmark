
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 7
    end_index = 7
    
    # Iterate through the list and add up the divisible integers
    for i in range(start_index, end_index + 1):
        if my_list[i] % 5 == 0 or my_list[i] % 7 == 0:
            sum += my_list[i]
    
    # Return the sum of the divisible integers
    return sum
