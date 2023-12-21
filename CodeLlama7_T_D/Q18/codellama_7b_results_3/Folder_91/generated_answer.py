
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables to keep track of the sum and the range of indices
    sum = 0
    start_index = 0
    end_index = len(my_list) - 1
    # Loop through the list from index 0 to index 4, both inclusive
    for i in range(start_index, end_index + 1):
        # If the current integer is divisible by either 8 or -3, add it to the sum
        if my_list[i] % 8 == 0 or my_list[i] % -3 == 0:
            sum += my_list[i]
    return sum
