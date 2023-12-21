
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 1
    end_index = 8
    # Iterate through the list and calculate the sum of all integers divisible by either -9 or -3 from index 1 to index 8, both inclusive. If no such integers exist in the specified range, the function should return 0.
    for i in range(start_index, end_index + 1):
        if my_list[i] % -9 == 0 or my_list[i] % -3 == 0:
            sum += my_list[i]
    # Return the calculated sum
    return sum
