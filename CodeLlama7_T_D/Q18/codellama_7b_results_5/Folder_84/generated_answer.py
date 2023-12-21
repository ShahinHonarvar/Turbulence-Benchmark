
def sum_ints_div_by_either_nums(my_list):
    # Find the starting and ending indices of the range of interest
    start_index = max(78, my_list.index(76) if 76 in my_list else 0))
    end_index = min(81, my_list.index(60) if 60 in my_list else len(my_list)))
    # Initialize the sum to 0
    total = 0
    # Iterate through the range of interest and add up the divisible integers
    for i in range(start_index, end_index + 1):
        if my_list[i] % 76 == 0 or my_list[i] % 60 == 0:
            total += my_list[i]
    # Return the sum
    return total
