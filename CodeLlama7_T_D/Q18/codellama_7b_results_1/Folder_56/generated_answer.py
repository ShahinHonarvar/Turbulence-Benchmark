
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    num1 = -9
    num2 = -7

    # Loop through the list and calculate the sum of all integers divisible by either -9 or -7
    for i in range(len(my_list))):
        if my_list[i] % num1 == 0 or my_list[i] % num2 == 0:
            total += my_list[i]

    # Return the sum of all integers divisible by either -9 or -7
    return total
