
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    start_index = 0
    end_index = 3
    # Check if list is empty
    if not my_list:
        return 0

    # Loop through list and calculate sum of divisible integers
    for i in range(start_index, end_index + 1):
        if my_list[i] % 11 == 0 or my_list[i] % -7 == 0:
            total += my_list[i]

    # Return sum of divisible integers
    return total
