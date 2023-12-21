
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    start_index = 25
    end_index = 70
    divisor1 = 74
    divisor2 = 15

    # Calculate sum of integers divisible by either 74 or 15 from index 25 to index 70, both inclusive.
    sum = 0
    for i in range(start_index, end_index + 1):
        if my_list[i] % divisor1 == 0 or my_list[i] % divisor2 == 0:
            sum += my_list[i]

    # Return sum of integers divisible by either 74 or 15 from index 25 to index 70, both inclusive.
    return sum
