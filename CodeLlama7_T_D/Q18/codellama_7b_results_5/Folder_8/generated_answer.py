
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 36
    end_index = 85
    # Iterate through the list and add up all integers divisible by either -27 or -96 from index 36 to index 85, both inclusive
    for i in range(start_index, end_index + 1):
        if my_list[i] % (-27) == 0 or my_list[i] % (-96) == 0:
            sum += my_list[i]
    # Return the sum
    return sum
