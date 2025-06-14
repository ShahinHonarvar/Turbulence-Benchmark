
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    start_index = 200
    end_index = 200
    # Iterate through the list and calculate the sum of all integers divisible by either 17 or -5
    for i in range(start_index, end_index + 1):
        if my_list[i] % 17 == 0 or my_list[i] % -5 == 0:
            total += my_list[i]
    # Return the sum of all integers divisible by either 17 or -5 from index 200 to index 200, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return total
