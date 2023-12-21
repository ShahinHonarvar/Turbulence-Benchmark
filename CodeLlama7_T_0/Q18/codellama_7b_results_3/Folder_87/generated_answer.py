
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 18
    end_index = 52
    # Iterate through the list and calculate the sum of all integers divisible by either 15 or 57 from index 18 to index 52, both inclusive
    for i in range(start_index, end_index + 1):
        if my_list[i] % 15 == 0 or my_list[i] % 57 == 0:
            sum += my_list[i]
    # Return the sum of all integers divisible by either 15 or 57 from index 18 to index 52, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
