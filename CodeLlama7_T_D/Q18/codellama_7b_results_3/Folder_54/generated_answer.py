 def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    start_index = 13
    end_index = 91
    # Iterate through the list and calculate the sum of all integers divisible by either -65 or -62 from index 13 to index 91, both inclusive.
    for i in range(start_index, end_index + 1):
        if my_list[i] % (-65) == 0 or my_list[i] % (-62) == 0:
            total += my_list[i]
    # Return the sum of all integers divisible by either -65 or -62 from index 13 to index 91, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return total
