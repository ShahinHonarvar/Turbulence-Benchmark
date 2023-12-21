
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 200
    end_index = 200
    # Iterate through the list and calculate the sum of divisible integers
    for i in range(start_index, end_index + 1):
        if my_list[i] % 17 == 0 or my_list[i] % -5 == 0:
            sum += my_list[i]
    # Return the sum of divisible integers
    return sum
