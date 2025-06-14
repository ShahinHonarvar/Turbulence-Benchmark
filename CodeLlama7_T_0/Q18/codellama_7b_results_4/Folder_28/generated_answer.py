
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 34
    end_index = 81
    # Iterate through the list and calculate the sum of all integers divisible by either 27 or 57
    for i in range(start_index, end_index + 1):
        if my_list[i] % 27 == 0 or my_list[i] % 57 == 0:
            sum += my_list[i]
    # Return the sum of all integers divisible by either 27 or 57 from index 34 to index 81, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
