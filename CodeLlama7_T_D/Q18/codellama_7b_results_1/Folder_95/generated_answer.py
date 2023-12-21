
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    start_index = 57
    end_index = 84
    sum = 0

    # Iterate through the list and calculate the sum of all integers divisible by either -30 or -88 within the specified range
    for i in range(start_index, end_index + 1):
        if my_list[i] % -30 == 0 or my_list[i] % -88 == 0:
            sum += my_list[i]

    # Return the sum of all integers divisible by either -30 or -88 within the specified range, or 0 if no such integers exist
    return sum
