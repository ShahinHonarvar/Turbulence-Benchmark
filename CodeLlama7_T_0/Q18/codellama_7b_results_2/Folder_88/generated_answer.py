
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 3
    end_index = 9

    # Iterate through the list and calculate the sum of all integers divisible by either 6 or 1
    for i in range(start_index, end_index + 1):
        if my_list[i] % 6 == 0 or my_list[i] % 1 == 0:
            sum += my_list[i]

    # Return the sum
    return sum
