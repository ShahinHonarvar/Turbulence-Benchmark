
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 55
    end_index = 66
    # Iterate through the list and calculate the sum of all integers divisible by either 22 or 82
    for i in range(start_index, end_index + 1):
        if my_list[i] % 22 == 0 or my_list[i] % 82 == 0:
            sum += my_list[i]
    # Return the sum of all integers divisible by either 22 or 82 from index 55 to index 66, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
