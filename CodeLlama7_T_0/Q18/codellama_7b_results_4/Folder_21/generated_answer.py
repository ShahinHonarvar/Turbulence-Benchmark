
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 315
    end_index = 934
    # Iterate through the list and calculate the sum of all integers divisible by either -897 or -556 from index 315 to index 934, both inclusive
    for i in range(start_index, end_index + 1):
        if my_list[i] % -897 == 0 or my_list[i] % -556 == 0:
            sum += my_list[i]
    # Return the sum of all integers divisible by either -897 or -556 from index 315 to index 934, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
