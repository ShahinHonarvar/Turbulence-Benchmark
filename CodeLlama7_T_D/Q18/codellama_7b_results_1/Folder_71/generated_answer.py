
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    start_index = 68
    end_index = 99
    divisor_1 = -37
    divisor_2 = -26

    # Calculate the sum of all integers in the specified range that are divisible by either -37 or -26
    sum = 0
    for i in range(start_index, end_index + 1):
        if my_list[i] % divisor_1 == 0 or my_list[i] % divisor_2 == 0:
            sum += my_list[i]

    # Return the sum
    return sum
