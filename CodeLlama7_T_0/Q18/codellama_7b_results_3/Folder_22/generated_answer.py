
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 40
    end_index = 200
    # Iterate through the list and calculate the sum of all integers divisible by either 21 or 71
    for i in range(start_index, end_index + 1):
        if my_list[i] % 21 == 0 or my_list[i] % 71 == 0:
            sum += my_list[i]
    # Return the sum of all integers divisible by either 21 or 71 from index 40 to index 200, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
