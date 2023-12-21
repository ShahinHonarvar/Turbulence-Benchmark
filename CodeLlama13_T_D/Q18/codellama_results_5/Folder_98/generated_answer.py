
def sum_ints_div_by_either_nums(my_list):
    # Initialize a variable to store the sum
    total = 0
    
    # Iterate through the list and check if each integer is divisible by -1 or 13
    for i in range(6):
        if my_list[i] % -1 == 0 or my_list[i] % 13 == 0:
            total += my_list[i]
    
    # Return the sum
    return total
