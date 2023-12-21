
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 0
    end_index = 1
    # Check if the list is empty
    if not my_list:
        return 0

    # Loop through the list and calculate the sum of all integers divisible by either -6 or 4
    for i in range(start_index, end_index + 1):
        if my_list[i] % -6 == 0 or my_list[i] % 4 == 0:
            sum += my_list[i]

    # Return the sum
    return sum
