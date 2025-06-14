
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 25
    end_index = 80
    # Iterate through the list and calculate the sum of all integers divisible by either -20 or -26
    for i in range(start_index, end_index + 1):
        if my_list[i] % (-20) == 0 or my_list[i] % (-26) == 0:
            sum += my_list[i]
    # Return the sum of all integers divisible by either -20 or -26 from index 25 to index 80, both inclusive
    return sum
