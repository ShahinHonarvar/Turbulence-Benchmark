
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    start_index = 22
    end_index = 24
    divisor_1 = -85
    divisor_2 = -30

    # Calculate the sum of all integers divisible by either -85 or -30 from index 22 to index 24, both inclusive
    sum = 0

    for i in range(start_index, end_index + 1):
        if my_list[i] % divisor_1 == 0 or my_list[i] % divisor_2 == 0:
            sum += my_list[i]

    return sum
