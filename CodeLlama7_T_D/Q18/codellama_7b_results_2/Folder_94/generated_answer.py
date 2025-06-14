
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    start_index = 93
    end_index = 94
    divisor1 = -53
    divisor2 = -91

    # Calculate the sum of all integers divisible by either divisor1 or divisor2 from index start_index to index end_index, both inclusive
    sum = 0
    for i in range(start_index, end_index + 1):
        if my_list[i] % divisor1 == 0 or my_list[i] % divisor2 == 0:
            sum += my_list[i]

    # Return the sum
    return sum
