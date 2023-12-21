
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    start_index = 22
    end_index = 24
    divisor_1 = -85
    divisor_2 = -30
    sum = 0

    # Check if the specified range is valid
    if (start_index < 0) or (end_index > len(my_list)) or (start_index >= end_index):
#        print("Invalid input")
        return 0

    # Iterate through the list and calculate the sum of all integers divisible by either -85 or -30
    for i in range(start_index, end_index + 1):
        if (my_list[i] % divisor_1 == 0) or (my_list[i] % divisor_2 == 0)):
            sum += my_list[i]

    # Return the calculated sum
    return sum
